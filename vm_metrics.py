from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CollectorRegistry
import psutil
import os

# Create a Flask app
app = Flask(__name__)

# Create a registry for custom metrics
registry = CollectorRegistry()

metric_name_prefix = os.getenv('METRIC_NAME', 'default')

# Define Prometheus metrics
cpu_used_gauge = Gauge('cpu_used', 'CPU usage in percentage', registry=registry)
ram_used_gauge = Gauge('ram_used', 'RAM usage percentage', registry=registry)
ram_available_gauge = Gauge('ram_available', 'RAM available percentage', registry=registry)

@app.route('/metrics')
def metrics():
    # Collect system stats
    cpu_used_gauge = Gauge(f'{metric_name_prefix}_cpu_used', 'CPU usage in percentage', registry=registry)
    ram_used_gauge = Gauge(f'{metric_name_prefix}_ram_used', 'RAM usage percentage', registry=registry)
    ram_available_gauge = Gauge(f'{metric_name_prefix}_ram_available', 'RAM available percentage', registry=registry)


    # Update Prometheus metrics
    cpu_used_gauge.set(cpu_used)
    ram_used_gauge.set(ram_used)
    ram_available_gauge.set(ram_available)

    # Generate and return the metrics in Prometheus format
    return Response(generate_latest(registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

