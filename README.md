# CloudOps Health Monitor

A Flask-based cloud health monitoring service packaged with Docker and designed for deployment on an Ubuntu AWS EC2 instance.

## Features

- Flask REST endpoints: `/`, `/health`, and `/system`
- Docker image with a non-root runtime user
- Docker health checks and restart policy
- Docker Compose deployment configuration
- Ubuntu EC2 deployment helper script
- GitHub Actions workflow for automated unit tests

## Architecture

```text
Browser
   |
   | HTTP :80
   v
AWS EC2 (Ubuntu Linux)
   |
   v
Docker Engine / Docker Compose
   |
   v
CloudOps Health Monitor
   |
   v
Flask + Gunicorn (:5000)
```

## Requirements

- Python 3.12+
- Docker
- Docker Compose plugin

## Run Locally

### Using Docker Compose

```bash
docker compose up -d --build
docker compose ps
```

Open:

- http://localhost/
- http://localhost/health
- http://localhost/system

Stop:

```bash
docker compose down
```

### Using Python

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000/health.

## Deploy to AWS EC2

1. Launch an Ubuntu EC2 instance.
2. Configure SSH access from your own IP and HTTP access if public access is required.
3. Connect through SSH:

```bash
ssh -i /path/to/your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

4. Install Git:

```bash
sudo apt-get update
sudo apt-get install -y git
```

5. Clone the repository:

```bash
git clone https://github.com/Anjalikumari458/cloudops.git
cd cloudops
```

6. Run the deployment script:

```bash
chmod +x scripts/deploy-ubuntu.sh
./scripts/deploy-ubuntu.sh
```

7. Verify:

```bash
sudo docker compose ps
sudo docker logs cloudops-health-monitor
curl http://localhost/health
```

Replace `YOUR_EC2_PUBLIC_IP` with your actual EC2 IP address.

**Security:** Never upload private SSH keys, AWS credentials, passwords, or other secrets to GitHub.

## Run Tests

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Useful Linux and Docker Commands

```bash
uname -a
df -h
free -h
top

docker images
docker ps
docker compose logs -f
docker compose restart
docker compose down
```

## Future Improvements

- HTTPS with TLS certificates
- Structured application logging and metrics
- Amazon ECR integration
- Automated AWS deployment using GitHub Actions
- Monitoring and alerting

## Project Status

This repository contains the Flask application, Docker configuration, automated tests, CI workflow, and EC2 deployment helper script.

AWS deployment must be performed and verified separately before claiming the application is live on AWS.