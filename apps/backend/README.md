# RepUp Backend (FastAPI)

🏋️‍♂️ **AI-Powered Gym Training Assistant Backend API**

## 🚀 Quick Start

### Local Development (Recommended)

```bash
# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker Development

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run individually
docker build -t repup-backend .
docker run -p 8000:8000 repup-backend
```

## 🔍 Health Check Endpoints

| Endpoint | Description | Response |
|----------|-------------|----------|
| `GET /` | Basic health status | Simple health info |
| `GET /health` | Standard health check | Service status |
| `GET /healthcheck` | **Comprehensive health check** | ✅ **Detailed system info** |

### ✅ Testing Commands

```bash
# Test all endpoints
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/healthcheck

# Check HTTP status codes
curl -w "HTTP Status: %{http_code}\n" http://localhost:8000/healthcheck
```

## 📋 Acceptance Criteria Status

- ✅ **`/healthcheck` endpoint available and returns 200**
- ✅ **Project runs locally with Docker**
- ✅ **FastAPI setup with proper structure**
- ✅ **Dockerfile optimized for production**
- ✅ **docker-compose.yml for easy development**

## 🧪 Testing Results

**✅ All Tests Passed Successfully!**

### Local Testing Results:
- ✅ FastAPI application starts successfully
- ✅ Virtual environment setup works
- ✅ All dependencies install correctly
- ✅ `/healthcheck` returns HTTP 200
- ✅ `/health` returns HTTP 200  
- ✅ `/` (root) returns HTTP 200
- ✅ JSON responses properly formatted
- ✅ System information correctly populated

### Docker Testing Results:
- ✅ Dockerfile builds successfully
- ✅ Docker image optimized and secure
- ✅ Health check endpoint configured
- ✅ Multi-service docker-compose ready

**🎯 Status: Production Ready!** All acceptance criteria met and tested.

## 🔧 Available Endpoints

### Health Check Endpoints

#### `GET /healthcheck` - **Comprehensive Health Check**
Returns detailed system information including:
- Service status and version
- System platform and architecture
- Memory and disk usage
- Python version and hostname
- Uptime since startup

**Example Response:**
```json
{
  "status": "healthy",
  "service": "repup-backend", 
  "version": "0.1.0",
  "timestamp": "2025-09-21T12:41:25.490527",
  "environment": "development",
  "uptime": "0d 0h 5m 32s",
  "system": {
    "platform": "Linux",
    "architecture": "x86_64", 
    "python_version": "3.12.3"
  },
  "memory": {
    "total": "11.68 GB",
    "available": "9.07 GB",
    "percentage": "22.4%"
  }
}
```