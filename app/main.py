
import os
from fastapi import FastAPI

app = FastAPI(
    title="Dockerized FastAPI Application",
    description="My first DevOps containerization project",
    version="1.0.0"
)

APP_NAME = os.getenv("APP_NAME", "My DevOps App")
APP_ENV = os.getenv("APP_ENV", "development")

@app.get("/")
def home():
    return {
        "message": "Welcome to my Dockerized FastAPI Application!",
        "app_name": APP_NAME,
        "environment": APP_ENV
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/about")
def about():
    return {
        "project": "Task 01 - Containerise an Application",
        "technology": ["Python", "FastAPI", "Docker"]
    }
