Dockerized Student Management System

This project is a simple 2-tier Student Management System built using Flask and MySQL and fully containerized using Docker and Docker Compose. The main goal of this project is to demonstrate backend development and Docker fundamentals in a clean and beginner-friendly way.

The application allows users to add student details through a web form. After submission, the homepage remains clean and does not display stored data. Student records can be viewed on a separate page. All services run inside Docker containers.

Architecture:
Browser -> Flask Application (Docker Container) -> MySQL Database (Docker Container)

Features:
- Add student details
- Fields include:
  - Full Name
  - Date of Birth
  - Degree (BE / BSc / BTech)
  - Year of Passing
  - Branch / Course
  - Email
  - Phone Number
- Homepage shows only the form
- Student data is displayed on a separate page
- Data is stored persistently using Docker volumes
- Fully containerized 2-tier application

Tech Stack:
- Backend: Python (Flask)
- Database: MySQL
- Containerization: Docker, Docker Compose
- Frontend: HTML, CSS (minimal)

Project Structure:
student-management-system/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       ├── index.html
│       └── students.html
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md

Prerequisites:
- Docker
- Docker Compose

To verify installation:
docker --version
docker-compose --version

How to Run the Project:

1. Clone the repository
git clone https://github.com/YashSV-cloud/dockerized-student-management-system.git
cd dockerized-student-management-system

2. Build and start the containers
docker-compose up --build

Wait for 20–30 seconds for the MySQL database to initialize.

3. Open the application in the browser
Add Student Page:
http://localhost:5000

View Students Page:
http://localhost:5000/students

4. Stop the containers
docker-compose down

To remove database data completely:
docker-compose down -v

Docker Concepts Used:
- Dockerfile to containerize Flask application
- Docker Compose for managing multiple containers
- Environment variables using .env file
- Docker volumes for MySQL data persistence
- Container-to-container communication using service names
- depends_on for service startup order

Error Handling:
- Database operations are handled using try-except blocks
- Prevents application crashes due to database errors
- Errors can be viewed using:
docker-compose logs web

Interview Explanation:
I built a Dockerized Student Management System using Flask and MySQL with a 2-tier architecture. The application and database run in separate Docker containers managed using Docker Compose, with persistent storage handled through Docker volumes.

Future Enhancements:
- Delete student records
- Search students by name
- Pagination for large datasets
- Docker health checks
- Cloud deployment

Author:
Yashwanth SV  
IT Student | Aspiring Data Analyst | DevOps Enthusiast

License:
This project is created for educational and learning purposes.
