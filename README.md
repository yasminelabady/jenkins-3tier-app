Jenkins 3-Tier Application Pipeline
This project demonstrates a simple CI/CD pipeline using Jenkins to build and run a 3-tier application with Docker Compose.

🧱 Project Structure
database/: MySQL Dockerfile and SQL initialization

backend/: Python Flask API that connects to MySQL

powerbi/: Simulated PowerBI frontend (e.g., simple dashboard)

docker-compose.yml: Defines and connects the three services

Jenkinsfile: Declarative pipeline for Jenkins automation

🚀 How to Set Up and Run the Pipeline
1. Install Prerequisites
Make sure the following are installed on your Jenkins host:
Docker
Git
Java 21+
Jenkins

2. Configure Jenkins
Create a New Pipeline Job:
Name: jenkins-3tier-app
Type: Pipeline
In the pipeline config:
Choose Pipeline script from SCM
SCM: Git
Repository URL:
https://github.com/yasminelabady/jenkins-3tier-app.git
Branch: main

3. Run the pipeline
Click "Build Now" in the job dashboard.
Jenkins will:
Checkout the code from GitHub.
Build the Docker images.
Start the 3 services using Docker Compose.

📂 File Structure

jenkins-3tier-app/
├── backend/           # Flask app
├── database/          # MySQL Dockerfile
├── powerbi/           # PowerBI placeholder
├── docker-compose.yml
└── Jenkinsfile



