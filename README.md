---

#  Weather Dashboard (FastAPI + Docker + AWS EC2)

A cloud-deployed weather application built using **FastAPI**, **Jinja2**, **Docker**, and hosted on **AWS EC2**.
I created this project as a **DevOps learning project** to understand cloud deployment, containerization, and hosting a real application on a public server.

---

##  Live Demo

 **Live App:** [http://52.206.36.54](http://52.206.36.54)
(Hosted on AWS EC2 — running inside a Docker container)

Search for any city like **New York**, **London**, **Tokyo**, **Bangalore**, etc.

---

##  Project Goals

This project helped me learn the complete DevOps workflow:

✔ Build a FastAPI backend
✔ Create a simple UI using HTML + Jinja
✔ Containerize the app with Docker
✔ Push the Docker image to Docker Hub
✔ Deploy and run the container on AWS EC2
✔ Inject API keys securely using environment variables
✔ Expose a public application on port 80

This is a great beginner-level cloud project showing **end-to-end deployment skills**.

---

##  Technologies Used

| Technology            | Purpose                      |
| --------------------- | ---------------------------- |
| **FastAPI**           | Backend API + HTML rendering |
| **Jinja2**            | Frontend templating          |
| **Docker**            | Containerization             |
| **Docker Hub**        | Image hosting                |
| **AWS EC2**           | Cloud server                 |
| **Amazon Linux 2023** | Server OS                    |
| **OpenWeather API**   | Weather data                 |

---

##  Project Structure

```
weather-dashboard/
│
├── app/
│   ├── main.py               # FastAPI backend logic
│   └── templates/
│       └── index.html        # UI (HTML + Jinja)
│
├── Dockerfile                # Docker build instructions
├── requirements.txt          # Python dependencies
├── .dockerignore             # Ignore files for Docker
└── README.md                 # Documentation
```

---

##  Docker Setup

### Build the Docker image:

```sh
docker build -t meghana2301/weather-dashboard:latest .
```

### Run locally:

```sh
docker run -p 8000:8000 meghana2301/weather-dashboard:latest
```

### Push to Docker Hub:

```sh
docker push meghana2301/weather-dashboard:latest
```

Docker image:
 [https://hub.docker.com/r/meghana2301/weather-dashboard](https://hub.docker.com/r/meghana2301/weather-dashboard)

---

##  Deployment on AWS EC2

I hosted the application on a **t2.micro (Free Tier)** Amazon Linux EC2 instance.

---

###  Install Docker on EC2

```bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
```

Logout and SSH back in.

---

###  Pull the Docker image

```bash
docker pull meghana2301/weather-dashboard:latest
```

---

###  Run the container (with API key)

```bash
docker run -d -p 80:8000 \
  -e OPENWEATHER_API_KEY="YOUR_API_KEY_HERE" \
  --name weather-app \
  meghana2301/weather-dashboard:latest
```

---

###  Verify the app is running

```bash
docker ps
```

---

##  Application Screenshot

Here is the Weather Dashboard running on AWS EC2:

<img src="https://private-user-images.githubusercontent.com/212178111/521694300-bb647bb1-5a01-41bd-be9e-c3ce8102b740.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQ3MzkyMDcsIm5iZiI6MTc2NDczODkwNywicGF0aCI6Ii8yMTIxNzgxMTEvNTIxNjk0MzAwLWJiNjQ3YmIxLTVhMDEtNDFiZC1iZTllLWMzY2U4MTAyYjc0MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMjAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTIwM1QwNTE1MDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNTYxYmYyZGI1Y2JhZDMyZGIwZDg2MGFmOGVkZDk5MzEwZWFlNTlmMjNhN2YzZmY1M2Q5ZTM0NmRhMjc4OWVhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2c2Pat7PxtApd_AmbG4_e5D7gbxBWUcY5iKj6MCUGX4" width="900"/>
---

##  How to Run Locally

### 1. Clone the repo:

```sh
git clone https://github.com/Meghana-0523/weather-dashboard.git
```

### 2. Install Python dependencies:

```sh
pip install -r requirements.txt
```

### 3. Create `.env` file:

```
OPENWEATHER_API_KEY=your_api_key_here
```

### 4. Start the server:

```sh
uvicorn app.main:app --reload
```

---

##  Contributions

This is a student project — improvements, suggestions, and pull requests are welcome!

---

##  License

This project is **open-source** and free to use.

---


