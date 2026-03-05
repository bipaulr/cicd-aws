from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 My CI/CD App</h1><p>Deployed automatically via GitHub Actions + AWS!</p>"

@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "App is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
