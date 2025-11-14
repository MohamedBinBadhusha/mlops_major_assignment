# 📘 MLOps Major Assignment  
### End-to-End MLOps Pipeline with GitHub Actions, Docker, and Kubernetes

This project implements a complete **MLOps pipeline** using:

- **Git + Branching Strategy**
- **GitHub Actions (CI/CD)**
- **Model Training & Evaluation (DecisionTreeClassifier on Olivetti Faces Dataset)**
- **Flask Web App for Inference**
- **Docker Image Packaging**
- **Docker Hub Deployment**
- **Kubernetes Deployment (3 replicas)**
- **NodePort Service Exposure**

---

## 📁 Branching Strategy

| Branch | Purpose |
|--------|----------|
| **main** | Initial setup (`README.md`, `.gitignore`) |
| **dev** | ML model development + CI/CD pipeline (train.py, test.py, ci.yml) |
| **docker_cicd** | Flask API, Dockerfile, Docker build & deployment, Kubernetes YAMLs |

The assignment required **no branch merges**, and all branches are maintained separately.

---

## 🧠 Dataset & Model

- **Dataset:** Olivetti Faces — loaded from `sklearn.datasets`
- **Model:** `DecisionTreeClassifier`
- **Train/Test Split:** 70% / 30%
- **Model Saved As:** `savedmodel.pth`
- **Evaluation:** Accuracy printed using `test.py`

---

## 🛠️ Project Structure

mlops_major_assignment/
│
├── train.py
├── test.py
├── savedmodel.pth
│
├── app.py # Flask inference app
├── templates/
│ └── index.html
│
├── Dockerfile
├── requirements.txt
│
├── deployment.yaml # Kubernetes Deployment (3 replicas)
├── service.yaml # Kubernetes NodePort Service
│
└── .github/workflows/ci.yml # GitHub Actions CI Pipeline


---

## ⚙️ GitHub Actions (CI Pipeline)

The workflow in **dev branch** performs:

1. **Checkout repository**
2. **Install dependencies**
3. **Run train.py** → generates model file
4. **Run test.py** → prints accuracy
5. **Ensures repo is functioning**

This validates the entire ML pipeline automatically.

---

## 🐳 Docker Containerization

A Dockerfile is provided to package the Flask app + model:

docker build -t mlops-flask-app .
docker tag mlops-flask-app <dockerhub-username>/mlops-flask-app:v1
docker push <dockerhub-username>/mlops-flask-app:v1


The image is available publicly on **Docker Hub** for Kubernetes to pull.

---

## ☸️ Kubernetes Deployment

### Deployment (`deployment.yaml`)

- 3 replicas
- pulls Docker Hub image
- exposes container port 5000

### Service (`service.yaml`)

- NodePort  
- Makes the Flask app accessible at:

http://localhost:30007


### Commands used:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get svc


---

## 🌐 Final Application

Once deployed, the web app becomes accessible via browser:
http://localhost:30007


You can upload an image → model predicts → output displayed.

---

## 📸 Screenshots (Included in PDF Submission)

The PDF contains all required screenshots:

- GitHub branches  
- train.py output  
- test.py accuracy  
- CI pipeline run  
- Docker build  
- Docker push  
- Docker Hub image  
- Kubernetes deployment  
- Running pods  
- Running service  
- Web app in browser  

---

## 📎 Repository & DockerHub Links

- **GitHub Repo:**  
  https://github.com/MohamedBinBadhusha/mlops_major_assignment

- **Docker Hub Image:**  
  `princebaja07/mlops-flask-app:v1`

---

## 👨‍🎓 Submitted By
**Mohamed Bin Badhusha E B**  
**Roll Number: g24ai2026**  
PGD Data Engineering – IIT Jodhpur  

