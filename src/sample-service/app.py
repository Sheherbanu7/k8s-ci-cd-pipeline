from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"service": "k8s-ci-cd-pipeline", "status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
