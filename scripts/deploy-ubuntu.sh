#!/usr/bin/env bash
set -euo pipefail

# Run this script on an Ubuntu EC2 instance after cloning this repository.
sudo apt-get update
sudo apt-get install -y ca-certificates curl

# Install Docker from Ubuntu's package repository for a simple learning setup.
sudo apt-get install -y docker.io docker-compose-v2
sudo systemctl enable --now docker

# Build and start the application. Port 80 on the EC2 security group must be open.
sudo docker compose up -d --build
sudo docker compose ps
echo "Deployment started. Open http://YOUR_EC2_PUBLIC_IP/health"
