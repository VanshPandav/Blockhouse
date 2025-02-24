
# Blockhouse Web App

A web application with a CI/CD pipeline using **GitHub Actions**, **Docker**, and **AWS EC2**. The app automatically builds, tests, and deploys to an EC2 instance on every push to the `master` branch.

---

## Features

- **CI/CD Pipeline**: Automated build, test, and deployment.
- **Docker**: Containerized FastAPI app.
- **AWS EC2**: Hosts the deployed app.
- **PostgreSQL**: Stores trade order data.

---

## 📡 API Endpoints

### 1. **Submit a Trade Order**
- **POST** `/submit_order`
- **Request:**

  ```json
  {
    "symbol": "JAY",
    "price": 250,
    "quantity": 20,
    "order_type": "buy"
  }
  ```
- **Response:**

  ```json
  {
    "symbol": "JAY",
    "price": 250.0,
    "quantity": 20,
    "order_type": "buy",
    "id": 4
  }
  ```

---

### 2. **Get All Orders**
- **GET** `/orders`
- **Response:**

  ```json
    [
      {
          "symbol": "ISH2",
          "price": 250.0,
          "quantity": 20,
          "order_type": "buy",
          "id": 1
      },
      {
          "symbol": "VAN",
          "price": 250.0,
          "quantity": 20,
          "order_type": "buy",
          "id": 2
      },
      {
          "symbol": "JAY",
          "price": 250.0,
          "quantity": 20,
          "order_type": "buy",
          "id": 3
      },
      {
          "symbol": "JAY",
          "price": 250.0,
          "quantity": 20,
          "order_type": "buy",
          "id": 4
      }
  ]
  ```

---

## ⚡ Deployment

1. **Build the Docker image:**

   ```bash
   docker build -t vanshpandav/blockhouse-web:latest .
   ```

2. **Run the container:**

   ```bash
   docker run -d -p 8080:8000 vanshpandav/blockhouse-web:latest
   ```

3. **Deploy to EC2:**

   ```bash
   ssh -i "path/to/private_key.pem" ubuntu@your-ec2-ip
   docker pull your-docker-username/blockhouse-web:latest
   docker run -d -p 8080:8000 your-docker-username/blockhouse-web:latest
   ```

---

## ✅ CI/CD Setup

Add these secrets to your GitHub repository:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `EC2_SSH_PRIVATE_KEY`
- `EC2_PUBLIC_IP`

The CI/CD pipeline is defined in `.github/workflows/deploy.yml`.

---

## 📚 Project Structure

```
.
├── .github/workflows/deploy.yml
├── app/
│   ├── main.py
│   └── models.py
├── Dockerfile
├── README.md
└── ...
```

---

## 🔗 Contact

- **Author**: [Vansh Pandav](https://www.linkedin.com/in/vansh-pandav-aab281141)  
- **Email**: vanshpandav@gmail.com  

---
