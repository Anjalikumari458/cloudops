from flask import Flask, jsonify
from datetime import datetime, timezone
import os
import platform
import socket

app = Flask(__name__)
STARTED_AT = datetime.now(timezone.utc).isoformat()

@app.get("/")
def home():
    return jsonify({
        "service": "CloudOps Health Monitor",
        "status": "running",
        "message": "Application is running inside a Docker container.",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "started_at": STARTED_AT
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "python_version": platform.python_version()
    }), 200

@app.get("/system")
def system_info():
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
