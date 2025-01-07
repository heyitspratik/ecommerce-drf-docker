# Define Docker Compose commands
DOCKER_COMPOSE=docker-compose
DOCKER_EXEC := $(DOCKER_COMPOSE) exec app
DOCKER_SERVICE=app

# Development server commands
up:
	$(DOCKER_COMPOSE) up -d

stop:
	$(DOCKER_COMPOSE) down

restart:
	$(DOCKER_COMPOSE) restart

logs:
	$(DOCKER_COMPOSE) logs -f

build:
	$(DOCKER_COMPOSE) build

shell:
	$(DOCKER_COMPOSE) exec $(DOCKER_SERVICE) sh

# Django management commands
manage:
	$(DOCKER_EXEC) python manage.py $(CMD)

# Migrations
makemigrations:
	$(DOCKER_EXEC) python manage.py makemigrations

migrate:
	$(DOCKER_EXEC) python manage.py migrate

superuser:
	$(DOCKER_EXEC) python manage.py createsuperuser

# Collect static files
collectstatic:
	$(DOCKER_EXEC) python manage.py collectstatic --noinput

# Add Demo User
demo-user:
	$(DOCKER_EXEC) python manage.py loaddata superuser.json

# Install dependencies
install:
	$(DOCKER_EXEC) pip install -r requirements.txt

# Run tests
test:
	$(DOCKER_EXEC) python manage.py test

# Clean up
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Shortcut for setting up the project
setup: install migrate collectstatic

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  up             Start containers"
	@echo "  down           Stop containers"
	@echo "  restart        Restart containers"
	@echo "  logs           View container logs"
	@echo "  manage CMD     Run Django management command"
	@echo "  makemigrations Create new migrations"
	@echo "  migrate        Apply database migrations"
	@echo "  collectstatic  Collect static files"
	@echo "  install        Install dependencies"
	@echo "  test           Run tests"
	@echo "  clean          Clean up *.pyc files"
	@echo "  setup          Set up project (install dependencies, migrate, collectstatic)"
	@echo "  help           Show this help message"
