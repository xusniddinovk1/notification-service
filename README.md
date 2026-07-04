# notification-service

Notification Service — a centralized backend service for sending Email, SMS, and In-App notifications built with Django + DRF, Celery, and Redis.

---

## Requirements

- Docker
- Docker Compose
- uv
- make (optional, recommended)

---

## Environment Variables

```bash
cp .env.example .env
# Fill in the required values
```

Key variables:

```env
SECRET_KEY=
DEBUG=True
DJANGO_SETTINGS_MODULE=config.settings.dev

REDIS_URL=redis://redis:6379/0

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
```

---

## Running the Project

### 1. Native (uv)

```bash
git clone https://github.com/xusniddinovk1/notification-service
cd notification-service

uv sync

uv run manage.py makemigrations
uv run manage.py migrate

uv run manage.py createsuperuser

uv run manage.py runserver
```

### 2. Docker Compose (Recommended)

```bash
docker compose -f docker/docker-compose.yml up -d
```

Starts 3 containers: `web`, `redis`, `celery`.

### 3. Makefile

```bash
make dev        # Run development server
make pre-prod   # Build and run via Docker
make stop       # Stop Docker containers
```

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/register/` | Register a new user |
| POST | `/api/v1/login/` | Login (returns JWT tokens) |
| POST | `/api/v1/token/refresh/` | Refresh access token |

### Channels
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/channels/` | List all channels |
| POST | `/api/v1/channels/` | Create a channel |
| GET | `/api/v1/channels/{id}/` | Get a channel |
| PUT | `/api/v1/channels/{id}/` | Update a channel |
| DELETE | `/api/v1/channels/{id}/` | Delete a channel |

### Templates
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/templates/` | List all templates |
| POST | `/api/v1/templates/` | Create a template |
| GET | `/api/v1/templates/{id}/` | Get a template |
| PUT | `/api/v1/templates/{id}/` | Update a template |
| DELETE | `/api/v1/templates/{id}/` | Delete a template |

### Preferences
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/preferences/` | List my preferences |
| POST | `/api/v1/preferences/` | Create a preference |
| PUT | `/api/v1/preferences/{id}/` | Update a preference |
| DELETE | `/api/v1/preferences/{id}/` | Delete a preference |

### Notifications
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/api/v1/notifications/` | List my notifications | User |
| GET | `/api/v1/notifications/{id}/` | Get a notification | User |
| POST | `/api/v1/notifications/send/` | Send a notification | Admin only |
| GET | `/api/v1/notifications/stats/` | Delivery statistics | Admin only |

---

## API Documentation

```
http://localhost:8000/api/schema/swagger-ui/
```

---

## Code Quality

```bash
uv run black .
uv run ruff .
uv run mypy .
uv run pytest .
```

All of the above can also be run via Makefile (recommended).

---

## Architecture

See [ARCHITECTURE.md](./ARCHITECTURE.md) for details on system design, layered architecture, and SOLID principles.