from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "application": "python-devops-cicd-cd",
        "hostname": socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({
        "health": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
