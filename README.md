# SCICSP-2025
LITOFF PREMIUM

Ứng dụng hỗ trợ tập gym bằng AI & Computer Vision, giúp người dùng tập đúng form, tránh chấn thương, theo dõi tiến bộ và kết nối cộng đồng gymbro.  

---

## 👥 Nhiệm vụ của từng nhóm

### 1. Frontend
- Phát triển ứng dụng di động (Flutter/React Native).  
- Tích hợp camera, overlay skeleton, cảnh báo sai form theo thời gian thực.  
- Luồng tập luyện: tạo session, đếm rep/set, theo dõi nghỉ.  
- Dashboard: theo dõi cân nặng, chỉ số cơ thể, biểu đồ tiến bộ.  
- Social: feed thành tích, thử thách, profile huấn luyện viên, notifications.  

### 2. Backend
- API (Auth, Users, Workouts, Exercises, Social, PT).  
- Lưu trữ & quản lý dữ liệu (Postgres, Redis, S3/GCS).  
- Realtime feedback qua WebSocket/Socket.IO.  
- Hệ thống thử thách, bảng xếp hạng, cộng đồng.  
- Bảo mật: OAuth2, JWT, TLS, phân quyền.  
- Hỗ trợ scaling, logging, monitoring.  

### 3. AI & Training
- Pose estimation (MediaPipe, MoveNet, OpenPose).  
- Phát hiện lỗi form, đếm rep/set theo bài tập.  
- Mapping nhóm cơ chính & phụ.  
- Pipeline: thu thập dữ liệu, tiền xử lý, training, evaluation, deploy (TFLite/Server GPU).  
- On-device inference cho máy mạnh, fallback server cho máy yếu.  

---

## 🏗️ Cấu trúc dự án
```
repup/
│
├── apps/ # Các ứng dụng chính
│ ├── mobile/ # Ứng dụng di động (Flutter/React Native)
│ ├── backend/ # API server + business logic
│ └── ai-service/ # Dịch vụ AI (inference, xử lý pose)
│
├── ml/ # Máy học: dữ liệu & training pipeline
│
├── infra/ # Hạ tầng: IaC, CI/CD, k8s deployment
│
└── docs/ # Tài liệu: API, thiết kế hệ thống, hướng dẫn
```

---

## 🔑 Công nghệ dự kiến
- **Mobile:** Flutter / React Native  
- **Backend:** Node.js (NestJS/Express) hoặc FastAPI/Django  
- **Database:** PostgreSQL + Redis  
- **Storage:** S3/GCS, CDN  
- **AI:** MediaPipe, MoveNet, OpenPose, TensorFlow/PyTorch  
- **Cloud:** Firebase / AWS / GCP  
- **Security:** OAuth2, JWT, TLS  

---

## 🚀 Lộ trình (Q2/2025)
- **Tuần 1–2:** Skeleton app, Auth, pose estimation baseline.  
- **Tuần 3–4:** Workout flow, sessions API, rep counter.  
- **Tuần 5–6:** Social feed, thử thách, PT hub.  
- **Tuần 7–8:** Dashboard tiến bộ, personalization.  
- **Tuần 9:** Stabilize, bảo mật, logging.  
- **Tuần 10:** Demo prototype (3 bài tập + feedback AI + social).  

---
