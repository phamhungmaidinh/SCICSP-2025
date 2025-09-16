# Architecture Overview

Components:
- Mobile app (Flutter/React Native) with camera + pose overlay
- Backend API (Express) for auth, workouts, social, trainers
- AI service for pose estimation and form analysis
- PostgreSQL + Redis

Data Flow:
- Mobile captures frames; on-device or sends to AI service
- AI returns pose + feedback; backend records reps/sets and history
- Social features through backend endpoints and WebSocket events

Security:
- OAuth2/JWT, TLS, role-based access, rate limiting
