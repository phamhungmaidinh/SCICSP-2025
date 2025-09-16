# RepUp – AI-Powered Gym Training Assistant

## 📖 Overview
**RepUp** (SCICSP-2025 – LITOFF PREMIUM) is a mobile app that leverages **AI & Computer Vision** to act as a personal gym trainer.  
It helps users:
- Maintain **correct form** to avoid injuries  
- Get **real-time AI feedback** during workouts  
- Automatically **count reps/sets**  
- **Track progress** (weight, body metrics, performance)  
- Join a **fitness community** with challenges, leaderboards, and trainers  
anh tien oc cho
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
```
🛠 Tech Stack

Mobile: Flutter / React Native

Backend: Node.js (NestJS/Express) or Python (FastAPI/Django)

Database: PostgreSQL, Redis

Storage: AWS S3 / GCS + CDN

AI: MediaPipe, MoveNet, OpenPose, TensorFlow, PyTorch

Deployment: Docker, Kubernetes, AWS/GCP, Firebase

Security: OAuth2, JWT, TLS

⚡ Setup Instructions
Prerequisites

Node.js (v18+) & npm/yarn

Python 3.9+

Flutter SDK or React Native CLI

Docker & Docker Compose

PostgreSQL & Redis

Git

1. Clone Repo
git clone https://github.com/phamhungmaidinh/SCICSP-2025.git
cd SCICSP-2025

2. Configure Environment

Copy environment files and adjust secrets:

cp apps/backend/.env.example apps/backend/.env
cp apps/mobile/.env.example apps/mobile/.env
cp apps/ai-service/.env.example apps/ai-service/.env

3. Install & Run Mobile App
cd apps/mobile
flutter pub get   # or yarn install (for React Native)
flutter run       # or npx react-native run-android / ios

4. Start Backend
cd apps/backend
npm install
npm run start:dev

5. Start AI Service
cd apps/ai-service
pip install -r requirements.txt
python inference.py --source webcam

6. Start Infrastructure (Optional)
docker-compose up -d
