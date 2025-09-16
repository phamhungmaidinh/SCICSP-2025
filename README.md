# RepUp – AI-Powered Gym Training Assistant

## 📖 Overview
**RepUp** (SCICSP-2025 – LITOFF PREMIUM) is a mobile app that leverages **AI & Computer Vision** to act as a personal gym trainer.  
It helps users:
- Maintain **correct form** to avoid injuries  
- Get **real-time AI feedback** during workouts  
- Automatically **count reps/sets**  
- **Track progress** (weight, body metrics, performance)  
- Join a **fitness community** with challenges, leaderboards, and trainers  

---

## ✨ Features

### Frontend (Mobile App)
- Cross-platform mobile app (Flutter or React Native)  
- Camera integration with **skeleton overlay**  
- Real-time form error detection & alerts  
- Workout session flow: create, start, rest, finish  
- Rep/set counting & rest timers  
- Dashboard for progress tracking  
- Social feed, challenges, trainer hub, notifications  

### Backend (API Server)
- REST/GraphQL APIs for Auth, Users, Workouts, Exercises, Social, Trainers  
- PostgreSQL for relational data, Redis for caching/session state  
- WebSockets (Socket.IO) for real-time feedback  
- Social features: feed, challenges, leaderboards  
- Security: OAuth2, JWT, TLS, role-based access  
- Scalable deployment with monitoring/logging  

### AI & Training
- Pose estimation with **MediaPipe**, **MoveNet**, or **OpenPose**  
- Form error detection & rep counting  
- Mapping primary & secondary muscle groups  
- ML pipeline: data collection → preprocessing → training → evaluation → deployment  
- On-device inference (TFLite) for strong devices, server fallback for weaker devices  

---

## 🏗 Project Structure
```plaintext
repup/
├── apps/              # Applications
│   ├── mobile/        # Flutter/React Native mobile app
│   ├── backend/       # API server
│   └── ai-service/    # AI inference service
│
├── ml/                # ML pipeline: data, training, notebooks
│
├── infra/             # Infrastructure: IaC, CI/CD, k8s deployment
│
└── docs/              # Documentation: API, design, guides
