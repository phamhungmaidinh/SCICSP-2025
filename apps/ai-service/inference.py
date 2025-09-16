import argparse
import os
from datetime import datetime

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv:
    load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(description="RepUp AI inference service placeholder")
    parser.add_argument("--source", default="webcam", choices=["webcam", "video", "image"], help="Input source")
    parser.add_argument("--model", default=os.getenv("MODEL_NAME", "movenet"), help="Model to use")
    parser.add_argument("--device", default=os.getenv("DEVICE", "cpu"), help="Device: cpu/cuda")
    parser.add_argument("--debug", action="store_true", help="Enable debug logs")
    return parser.parse_args()


def main():
    args = parse_args()
    ts = datetime.utcnow().isoformat()
    print(f"[{ts}] Starting AI service with model={args.model}, source={args.source}, device={args.device}")
    print("This is a placeholder. Integrate MediaPipe/MoveNet/OpenPose here.")


if __name__ == "__main__":
    main()
