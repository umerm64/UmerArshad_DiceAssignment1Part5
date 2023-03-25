from flask import Flask
import os
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

@app.route('/')
def home():
    return "Hello, World"

@app.route("/metrics")
def hello():
    return jsonify(say_hello())
def say_hello():
    return {"message": "hello"}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
