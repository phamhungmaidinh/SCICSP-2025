# RepUp Mobile App

This folder will contain the cross-platform mobile app. You can choose either:

- Flutter
- React Native

Getting started:

1) Decide the stack (Flutter or React Native).
2) Initialize the project in this directory (`apps/mobile`).
3) Use `.env` for API base URL and feature flags.

Example env keys:

```
API_BASE_URL=http://localhost:3000
SENTRY_DSN=
FEATURE_AI_ON_DEVICE=true
```

Notes:
- Camera integration will render pose skeleton and show real-time feedback.
- Use WebSocket to receive AI feedback when using server-side inference.
