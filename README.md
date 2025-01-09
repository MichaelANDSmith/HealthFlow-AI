# HealthFlow AI

HealthFlow AI is an intelligent personal assistant platform designed to enhance personal well-being by offering comprehensive support for daily time management, health advice, and personalized recommendations. Leveraging cutting-edge natural language processing (NLP) and deep learning techniques, HealthFlow AI can intelligently recognize user needs and provide tailored suggestions to optimize daily routines and promote healthy living.

## Features

- **Personalized Time Management**: Generate customized daily schedules based on your work hours, breaks, and preferences.
- **Health Advice**: Receive personalized health tips and recommendations based on your age, activity level, and lifestyle.
- **AI-Powered Recommendations**: Get insightful suggestions for improving productivity, maintaining a healthy lifestyle, and optimizing your daily routines.
- **NLP Integration**: Understand and analyze user input via natural language processing for better interaction and response.

## Tech Stack

- **Backend Framework**: Flask
- **Database**: PostgreSQL / SQLAlchemy
- **Asynchronous Tasks**: Celery
- **Authentication**: JWT (JSON Web Tokens)
- **AI/ML**: Transformers (Hugging Face) for NLP tasks
- **Containerization**: Docker (Optional)

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL (or any other supported relational database)
- Redis (for Celery)

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/HealthFlow-AI.git
    cd HealthFlow-AI
    ```

2. Install Dependencies
    Create a virtual environment and install the required dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For macOS/Linux
    # or
    venv\Scripts\activate     # For Windows

    pip install -r requirements.txt
    ```

3. Set Up Environment Variables
    Create a .env file in the project root and configure the following variables:
    ```bash
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgresql://username:password@localhost/healthflow
    CELERY_BROKER_URL=redis://localhost:6379/0
    CELERY_RESULT_BACKEND=redis://localhost:6379/0
    JWT_SECRET_KEY=your_jwt_secret_key
    ```

4. Run Database Migrations
    To set up the database, run the following commands:
    ```bash
    python run.py
    ```
5. Start the Application
    Run the Flask development server:
    ```bash
    flask run
    ```
6. Run Celery (for asynchronous tasks)
    In a separate terminal, run Celery worker:
    ```bash
    celery -A app.tasks.celery worker
    ```
## API Endpoints
### 1. POST /auth/register
**Request Body:**
    ```json
    {
      "username": "john_doe",
      "email": "john.doe@example.com",
      "password": "yourpassword"
    }
    ```
**Response:**
    ```json
    {
      "message": "User john_doe created successfully"
    }
    ```
### 2. POST /auth/login
Login to get a JWT token.
**Request Body:**
    ```json
    {
      "email": "john.doe@example.com",
      "password": "yourpassword"
    }
    ```
**Response:**
    ```json
    {
      "access_token": "your_jwt_token"
    }
    ```
### 3. POST /time/get_schedule
Get a personalized daily schedule based on user input.
**Request Body:**
    ```json
    {
      "work_hours": 8,
      "breaks": ["lunch", "coffee break"],
      "preferences": "morning workouts"
    }
    ```
**Response:**
    ```json
    {
      "morning": "Work on project",
      "afternoon": "Take a break and do some exercise",
      "evening": "Relax and meditate"
    }
    ```
### 4. POST /health/get_health_advice
Get personalized health advice.
**Request Body:**
    ```json
    {
      "age": 30,
      "activity_level": "moderate",
      "diet": "balanced"
    }
    ```
**Response:**
    ```json
    {
      "advice": "Drink plenty of water throughout the day."
    }
    ```
### 5. POST /recommendation/get_recommendations
Get personalized recommendations based on user data.
**Request Body:**
    ```json
    {
      "goals": ["lose weight", "improve productivity"]
    }
    ```
**Response:**
    ```json
    {
      "recommendations": [
      "Try a new healthy recipe for lunch today.",
      "Set a goal to walk 10,000 steps this week."
       ]
    }
    ```
## Running Tests
To run tests, use the following command:
    ```bash
       pytest
    ```
Make sure you have your environment variables set up before running tests.

## Docker Setup (Optional)
To containerize the application using Docker, follow these steps:
1. Build the Docker Image
    ```bash
    docker build -t healthflow-ai 
    ```

2. Run the Docker Container
    Create a virtual environment and install the required dependencies:
    ```bash
    docker run -d -p 5000:5000 healthflow-ai
    # or
    venv\Scripts\activate     # For Windows

    pip install -r requirements.txt
    ```

3. Docker Compose (Optional)
    You can also use docker-compose to set up the environment, including Redis and PostgreSQL.     Create a docker-compose.yml file in the root directory:
    ```yaml
    version: '3'

    services:
 web:
   build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://username:password@db/healthflow
      - CELERY_BROKER_URL=redis://redis:6379/0
      - JWT_SECRET_KEY=your_jwt_secret_key
    depends_on:
      - db
      - redis

  db:
    image: postgres:latest
    environment:
      - POSTGRES_USER=username
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=healthflow

  redis:
    image: redis:latest
    ```
Then run:
```bash
   docker-compose up --build
    ```
## Contributing
We welcome contributions! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.

### Steps for Contributing:
1. Fork the repository.
2. Create a new feature branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

## License
HealthFlow AI is licensed under the MIT License.