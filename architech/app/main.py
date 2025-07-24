from fastapi import FastAPI, Response
from time import time
import os
import getpass
app = FastAPI()

start_time = time()


@app.get("/", tags=["Root"])
def read_root():
    # Try to get the app starter's name from environment or system
    starter = os.environ.get("APP_STARTER") or getpass.getuser() or "there"
    return {"message": f"Hello, {starter}!"}

@app.get("/greet", tags=["Greet"])
def greet(name: str = "Guest", title: str = None):
    """
    Advanced greet endpoint. Optionally pass ?name=YourName&title=Dr for a custom greeting.
    """
    if title:
        greeting = f"Hello, {title} {name}!"
    else:
        greeting = f"Hello, {name}!"
    return {"greeting": greeting}

@app.get("/greet/{name}", tags=["Greet"])
def greet_path(name: str, title: str = None):
    """
    Greet by path parameter, e.g. /greet/Alice?title=Ms
    """
    if title:
        greeting = f"Hello, {title} {name}!"
    else:
        greeting = f"Hello, {name}!"
    return {"greeting": greeting}

try:
    import psutil
except ImportError:
    psutil = None

@app.get("/metrics/performance", tags=["Metrics"])
def performance_metrics():
    """
    Returns basic memory and CPU usage info (if psutil is installed).
    """
    if not psutil:
        return {"error": "psutil not installed. Run 'pip install psutil' for performance metrics."}
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0.1)
    return {
        "memory_total_mb": round(mem.total / 1024 / 1024, 2),
        "memory_used_mb": round(mem.used / 1024 / 1024, 2),
        "memory_percent": mem.percent,
        "cpu_percent": cpu
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Basic health check endpoint."""
    return {"status": "ok"}

@app.get("/metrics/uptime", tags=["Metrics"])
def uptime():
    """Returns the uptime of the application in seconds."""
    return {"uptime_seconds": round(time() - start_time, 2)}

