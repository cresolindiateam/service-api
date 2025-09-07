from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/api/hello")
def hello():
    return jsonify(service="api", branch="develop", msg="Hello from API! New 4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
