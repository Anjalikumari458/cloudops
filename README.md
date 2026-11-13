# CloudOps Health Monitor

A small Flask service packaged with Docker and designed for deployment on an Ubuntu EC2 virtual machine. It demonstrates a practical cloud deployment workflow: build an image, run a container, expose an HTTP endpoint, and check application health.

## Features

- Flask REST endpoints: `/`, `/health`, and `/system`
- Docker image with a non-root runtime user
- Docker health check and restart policy
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
CloudOps Health Monitor container
  |
  v
Flask + Gunicorn (:5000)
```

## Run locally

Requirements: Python 3.12+ and Docker with the Compose plugin.

### Option A: Docker Compose

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

### Option B: Python

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000/health.

## Deploy to AWS EC2 (Ubuntu)

1. In AWS Console, launch an Ubuntu Server EC2 instance for learning.
2. In its Security Group, allow **SSH (TCP 22) only from your own public IP**. Add **HTTP (TCP 80) from the internet** only if you want the demo publicly reachable.
3. Connect using the SSH command shown by AWS. For an Ubuntu AMI, the username is usually `ubuntu`:

```bash
ssh -i /path/to/your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

4. Install Git and clone your repository:

```bash
sudo apt-get update
sudo apt-get install -y git
git clone https://github.com/YOUR_USERNAME/cloudops-health-monitor.git
cd cloudops-health-monitor
```

5. Run the deployment helper:

```bash
chmod +x scripts/deploy-ubuntu.sh
./scripts/deploy-ubuntu.sh
```

6. Verify:

```bash
sudo docker compose ps
sudo docker logs cloudops-health-monitor
curl http://localhost/health
```

Then open `http://YOUR_EC2_PUBLIC_IP/health` in your browser.

> Replace `YOUR_USERNAME` and `YOUR_EC2_PUBLIC_IP` with your own values. Do not upload your private `.pem` key, AWS access keys, passwords, or other secrets to GitHub.

## Run tests

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Useful Linux and Docker commands

```bash
# Linux/server
uname -a
df -h
free -h
top

# Docker
docker images
docker ps
docker compose logs -f
docker compose restart
docker compose down
```

## Project scope and honest status

This repository provides the application, container configuration, tests, CI workflow, and an EC2 deployment script. The AWS deployment is **not performed automatically** by uploading this repository. Complete the EC2 steps above and verify the public health endpoint before describing it as deployed on AWS.

## Possible improvements

- Add HTTPS with a reverse proxy and TLS certificate
- Add structured application logging and metrics
- Push versioned images to Amazon ECR
- Deploy through GitHub Actions using securely stored GitHub Secrets or AWS OIDC
- Add monitoring and alerting
