# Boilerplate for FastAPI, MongoDB, Motor Projects
![Python3.11.2](https://img.shields.io/badge/Python-3.11.2-brightgreen.svg?style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-6.0-brightgreen.svg?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.92.0-brightgreen.svg?style=flat-square)
![Motor](https://img.shields.io/badge/Motor-3.1.1-brightgreen.svg?style=flat-square)


## Features
A new backend project created with this boilerplate provides:
- [x] Asynchronous high-performance RESTful APIs built upon [FastAPI](https://fastapi.tiangolo.com/) framework.
- [x] Asynchronous CRUD operations for a sample resource built upon [Motor](https://motor.readthedocs.io/en/stable/) driver for MongoDB, providing high performance and efficiency.
- [x] API documentation with [Swagger UI](https://swagger.io/tools/swagger-ui/).
- [x] API testing with [pytest](https://docs.pytest.org/en/7.1.x/) and [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio).
- [x] Dockerfile for containerization and docker-compose support.
- [x] Easy creation of new backend services with [cookiecutter](https://github.com/cookiecutter/cookiecutter).
- [x] Easy package menagement with [Poetry](https://python-poetry.org/).
- [x] Health API for service health checking.
- [x] Easy configuration with environment variables.
- [x] Easy testing, develop running, docker build, docker-compose up and down with Makefile.
- [x] Proper logging with ID masking.

## Prerequisites
- Python 3.11+
- [Poetry](https://python-poetry.org/) installed
- Docker installed
- GNU Make

## Getting Started

### Edit Environment Variables
Edit the `.env` file within the project folder.

### Run Tests
```sh
make test
```
(This may not work at this time. Please use docker-compose instead.)

### Build Docker Image
```sh
make docker-build
```

### Docker-compose
```sh
make docker-compose-up
make docker-compose-down
```

### Run Service Locally
```sh
make dev
```
This will create a MongoDB container as well.
(This may not work at this time. Please use docker-compose instead.)

### Check Swagger API Document
Go to ` http://localhost:8888/docs`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you.

## Credit: 
Forked from https://github.com/klee1611/cookiecutter-fastapi-mongo