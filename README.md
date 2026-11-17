
# Dockerized FastAPI Application

## Project Overview

This project demonstrates how to containerize a Python FastAPI application using Docker.

It was developed as Task 01 for the UpStartInterns DevOps Engineering Internship.

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Docker

## Project Structure

```text
fastapi-docker-project/
├── app/
│   └── main.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Features

- FastAPI REST API
- Health check endpoint
- Environment variable configuration
- Docker containerization
- Interactive API documentation

## Build and Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fastapi-docker-project
```

### 2. Build Docker image

```bash
docker build -t fastapi-devops-app .
```

### 3. Run the container

```bash
docker run -d --name fastapi-devops-container -p 8000:8000 -e APP_NAME="UpStartInterns DevOps Project" -e APP_ENV="production" fastapi-devops-app
```

## Access the Application

- Home: http://localhost:8000/
- Health: http://localhost:8000/health
- About: http://localhost:8000/about
- API Docs: http://localhost:8000/docs

## Stop the Container

```bash
docker stop fastapi-devops-container
docker rm fastapi-devops-container
```

## Learning Outcome

Learned how to build Docker images, configure environment variables, run containers, and deploy a FastAPI application inside Docker.

## Internship

UpStartInterns - DevOps Engineering
