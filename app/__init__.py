from flask import Flask
from pyctuator.pyctuator import Pyctuator
import psutil
import threading
import time
from app.views import views_bp

app = Flask(__name__)

app.register_blueprint(views_bp)

pyctuator = Pyctuator(
    app,
    "Flask Actuator Service",
    app_url="http://localhost:5000",
    pyctuator_endpoint_url="http://localhost:5000/actuator",
    registration_url=None
)

# Example health check
def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > 90:
        return "Disk space usage is critical", False
    return "Disk space usage is ok", True

pyctuator.register_health_provider(check_disk_space)

# Example metrics collection
def collect_metrics():
    while True:
        pyctuator.metrics.set_gauge(
            "custom_metric.cpu_usage",
            psutil.cpu_percent(interval=1),
            "CPU usage percentage"
        )
        time.sleep(10)

threading.Thread(target=collect_metrics).start()
