# E-Commerce RESTful API

## Features
- View Products
- Add Products
- Place Orders

## Setup

## Prerequisites
Before getting started, ensure you have the following installed:

- Install Docker: **[Docker](https://docs.docker.com/get-docker/)**
- Install Docker Compose: **[Docker Compose](https://docs.docker.com/compose/install/)**
- Install Make (make is used to automate tasks like building containers, running migrations, etc):
  
  ```bash
  sudo apt-get update
  sudo apt-get install make
  ```

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Build the Docker Containers
The project uses Docker for containerization. You can build and start the containers with the following commands:

```bash
make build
make stop && make up
```

This will:

Build the Docker images based on the Dockerfile.
Start the containers defined in docker-compose.yml.


### 3. Install Dependencies
The project uses a requirements.txt file for Python dependencies. The Docker container will automatically install these when it starts, but you can manually install dependencies by running:

```bash
docker-compose exec app pip install -r requirements.txt
```


### 4. Create Database and Apply Migrations
To set up the database and apply any migrations, run:

```bash
make makemigrations
make migrate
```

### 5. Create a Superuser
To access the Django admin panel, you'll need to create a superuser. Run the following command inside the Docker container:

bash
```
make createsuperuser
```
Follow the prompts to create the superuser.

### 6. Access the Application
Once everything is set up, you can access the application at:

Django Admin Panel: http://127.0.0.1:8000/admin

API Endpoints: http://127.0.0.1:8000/api


### 7. Stopping the Containers
To stop the Docker containers, run:

```bash
make stop
```


### 8. Additional Commands

Restart the Docker containers (if needed):

```bash
make restart
```

To check logs:
```bash
make logs
```

Rebuild the Docker containers (if needed):

```bash
make build
```

### Run tests:

```bash
make test
```

## Project Structure
- **`app/`**: Main application code (Django app).
- **`Dockerfile`**: Docker configuration file.
- **`docker-compose.yml`**: Docker Compose configuration to set up services (e.g., app, db).
- **`Makefile`**: Makefile to simplify common tasks (build, migrate, stop, etc.).
- **`requirements.txt`**: Python dependencies for the project.
