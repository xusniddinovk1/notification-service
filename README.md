# notification-service
Notification Service — email, SMS va in-app xabarlarni markazlashtirib yuboruvchi backend tizim.

# 0. Requirements
    Docker
    Docker-compose
    Make
    uv

# 0.1 Environment Variables
* (dev mode) Required environment variables
```bash
copy .env.example .env
nano .env  # Insert all the required values
```

* (prod mode) Required environment variables
```bash
copy .env.example .env
nano .env  Insert all the required values
```

# 1. Running the Project

## 1.1. Native running (uv)
1.
```bash
git clone https://github.com/xusniddinovk1/notification-service
```
2.
```bash
cd notification-service
```
3. Sync dependencies
```bash
uv sync
```
4. Create migrations
```bash
uv run manage.py makemigrations
```
5. Run migrations
```bash
uv run manage.py migrate
```
6. Create superuser
```bash
uv run manage.py createsuperuser
```
7. Start the server
```bash
uv run manage.py runserver
```

## 1.2 Docker/docker-compose running

1. Docker compose
```bash
docker-compose -f ./docker/docker-compose.yaml up -d
```
2. Docker 
```bash
docker rm notification-service
docker run -d -p 8000:8000 notification-service
```

## 1.3 Makefile (Recommended)

1. For development
```bash
make dev
```
2. For test development(pre-prod)
```bash
make pre-prod
```

# 2. Code Quality and Testing

## 2.1 Linters

1. Black
```bash
uv run black .
```
2. Ruff
```bash
uv run ruff .
```
3. Mypy
```bash
uv run mypy .
```

## 2.2 Testing

1. Pytest
```bash
uv run pytest .
```

All of the above can also be run via Makefile (recommended)