
from fastapi import FastAPI

app = FastAPI(
    title="Task Management API",
    description="A cloud-native task management service",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Task Management API is running",
        "status": "healthy"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [],
        "total": 0
    }
