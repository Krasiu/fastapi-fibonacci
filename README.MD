# Fibonacci API

Demo project built on top of FastAPI with Celery (RabbitMQ as broker, SQLite as backend). Wrapped together with Docker.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Only requirement is Docker installed and running on your machine. If you want to run the tests locally first, you'll need Python 3.7+ as well.

### Installing


Clone this repository:
```
git clone https://github.com/Krasiu/fastapi-fibonacci.git
cd fastapi-fibonacci
```

Optionally, you can run the tests:
```
pip install -r requirements.txt
python -m pytest
```

Run docker-compose to start services:
```
docker-compose up
```

You can open http://127.0.0.1:8000/ in your browser, and you should see: 
```
{"Hello": "Fibonacci"}
```
## API
API exposes two endpoints:
```
GET /fibonacci/{int}
- allows to get first n numbers of Fibonacci sequence,
- underlying method is artificially slowed down,
- immediately returns task id & onloads the work via Celery. 
    
GET /tasks/{uuid}
- allows to get current state of task,
- immedietely returns task status and results (if available).
```
