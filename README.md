
# Blockhouse Backend Service

This project is a backend service for handling trade order submissions, built using Python (FastAPI) and containerized with Docker. The service is deployed on an AWS EC2 instance, with CI/CD pipelines set up using GitHub Actions.

## Features

- **Trade Order Management:** Submit and retrieve trade orders.
- **Docker Integration:** Containerized app for easy deployment.
- **CI/CD Pipeline:** Automated build and deployment process using GitHub Actions.
- **AWS Deployment:** Hosted on an EC2 instance, listening on port 8000.

## API Endpoints

Base URL: `http://3.133.141.29:8000`

- **Submit an order (POST):**
  - Endpoint: `/orders`
  - Request Body (JSON):
    ```json
    {
      "order_id": "12345",
      "symbol": "AAPL",
      "quantity": 10,
      "price": 150.5
    }
    ```
  - Response (JSON):
    ```json
    {
      "symbol": "JAY",
      "price": 250,
      "quantity": 20,
      "order_type": "buy"
    }
    ```

- **Retrieve all orders (GET):**
  - Endpoint: `/orders`
  - Response (JSON):
    ```json
    [
      {
        "order_id": "12345",
        "symbol": "AAPL",
        "quantity": 10,
        "price": 150.5
      }
    ]
    ```

## Running the Project

### Prerequisites

Ensure you have the following installed:
- Docker
- Git

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vanshpandav/blockhouse.git
   cd blockhouse
   ```

2. **Access the API:**
   Open your browser or use Postman to test the endpoints:
   - GET: [http://localhost:8000/orders](http://localhost:8000/orders)
   - POST: [http://localhost:8000/orders](http://localhost:8000/orders)

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions and runs on every push to the `master` branch. It performs the following steps:
- **Build Docker image**
- **Push to Docker Hub**
- **Deploy to EC2 instance**

## Deployment

The backend is deployed on an EC2 instance, accessible at:
[http://3.133.141.29:8000](http://3.133.141.29:8000)


## Author

**Vansh Pandav**  
- LinkedIn: [Vansh Pandav](https://www.linkedin.com/in/vansh-pandav-aab281141)  
- GitHub: [vanshpandav](https://github.com/vanshpandav)
