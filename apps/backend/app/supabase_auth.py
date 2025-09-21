import os
import time
from typing import Any, Dict, Optional

import httpx
from jose import jwt, jwk
from jose.utils import base64url_decode
from supabase import create_client, Client


class SupabaseAuth:
    def __init__(self, supabase_url: str) -> None:
        self.supabase_url = supabase_url.rstrip("/")
        self.jwks_url = f"{self.supabase_url}/auth/v1/jwks"
        self._jwks: Optional[Dict[str, Any]] = None
        self._jwks_fetched_at: float = 0.0
        self._jwks_ttl: float = 60 * 60  # 1 hour

    async def get_jwks(self) -> Dict[str, Any]:
        now = time.time()
        if self._jwks and now - self._jwks_fetched_at < self._jwks_ttl:
            return self._jwks

        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(self.jwks_url)
            r.raise_for_status()
            self._jwks = r.json()
            self._jwks_fetched_at = now
            return self._jwks

    async def verify(self, token: str) -> Dict[str, Any]:
        jwks = await self.get_jwks()
        try:
            headers = jwt.get_unverified_header(token)
        except Exception as e:
            raise e
        kid = headers.get("kid")
        if not kid:
            raise ValueError("JWT missing kid header")

        # Find matching key
        key_dict = None
        for k in jwks.get("keys", []):
            if k.get("kid") == kid:
                key_dict = k
                break
        if not key_dict:
            raise ValueError("No matching JWK for kid")

        public_key = jwk.construct(key_dict)
        message, encoded_sig = str(token).rsplit(".", 1)
        decoded_sig = base64url_decode(encoded_sig.encode("utf-8"))
        if not public_key.verify(message.encode("utf-8"), decoded_sig):
            raise ValueError("Signature verification failed")

        # Signature OK, now decode (skip signature verification to avoid rebuilding key)
        payload = jwt.get_unverified_claims(token)
        # Optional: validate exp
        if "exp" in payload and time.time() > float(payload["exp"]):
            raise ValueError("Token has expired")
        return payload


def get_supabase_env() -> Dict[str, str]:
    return {
        "SUPABASE_URL": os.environ.get("SUPABASE_URL", ""),
        "SUPABASE_ANON_KEY": os.environ.get("SUPABASE_ANON_KEY", ""),
        "SUPABASE_SERVICE_ROLE_KEY": os.environ.get("SUPABASE_SERVICE_ROLE_KEY", ""),
    }


def create_supabase_client() -> Client | None:
    env = get_supabase_env()
    url = env.get("SUPABASE_URL")
    key = env.get("SUPABASE_SERVICE_ROLE_KEY") or env.get("SUPABASE_ANON_KEY")
    if url and key:
        return create_client(url, key)
    return None
