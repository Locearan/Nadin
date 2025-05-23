from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
import time
import random
registry = CollectorRegistry()
REQUEST_COUNT = Counter(
    'app_request_count',
    'Total number of requests to the application',
    ['method', 'endpoint'],
    registry=registry
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint'],
    registry=registry
)
app = Flask(__name__)
@app.route('/')
def hello():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    # Simulate some work
    time.sleep(random.uniform(0.01, 0.1))
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint='/').observe(latency)
    return "Hello, World from our Python Web Service!"
@app.route('/heavy')
def heavy_task():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/heavy').inc()
    # Simulate a heavier task
    time.sleep(random.uniform(0.1, 0.5))
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint='/heavy').observe(latency)
    return "Heavy task completed!"
@app.route('/metrics')
def metrics():
    REQUEST_COUNT.labels(method='GET', endpoint='/metrics').inc()
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)