# Architecture

## Purpose

Notification Service is a standalone backend microservice for sending notifications. In a real-world setup, it is called by other backend services (e.g. banking app, e-commerce platform) — not directly by end users.

## Tech Stack

- **Framework**: Django 6 + Django REST Framework
- **Authentication**: SimpleJWT
- **Async Queue**: Celery + Redis
- **Database**: PostgreSQL (SQLite for dev)
- **Template Engine**: Jinja2
- **Email**: Gmail SMTP via `django.core.mail`
- **API Docs**: drf-spectacular (Swagger UI)
- **Containerization**: Docker + Docker Compose
- **Dependency Manager**: uv

## Layered Architecture

Each app follows a strict 4-layer architecture:

```
View → Serializer → Service → Repository → Model
```

- **View** — handles HTTP request/response only
- **Serializer** — validates and transforms input/output data
- **Service** — business logic (preference checks, token generation, etc.)
- **Repository** — database operations only, no business logic
- **Model** — data structure

## Dependency Injection

Manual DI is used via `container.py` in each app. Services never instantiate repositories directly — dependencies are injected via constructors:

```python
class NotificationService:
    def __init__(self, repo: NotificationRepository, preference_repo: UserPreferenceRepository):
        self.repo = repo
        self.preference_repo = preference_repo
```

```python
# container.py
def get_notification_service() -> NotificationService:
    return NotificationService(
        repo=NotificationRepository(),
        preference_repo=UserPreferenceRepository(),
    )
```

## Async Notification Flow

Sending emails/SMS can take 2-5 seconds. Celery handles this asynchronously so the API responds immediately:

```
POST /api/v1/notifications/send/
        ↓
View validates request
        ↓
Service checks user preference → creates Notification (status=PENDING)
        ↓
Celery task pushed to Redis queue → API returns 201
        ↓ (background)
Celery renders template → sends email/SMS → updates status to SENT/FAILED
```

Retry on failure (exponential backoff):
```python
@app.task(bind=True, max_retries=3)
def send_notification_task(self, notification_id):
    try:
        ...
    except Exception as exc:
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)
```

## Template Rendering

Templates support dynamic variables via Jinja2:

```
Template: "Hello {{ first_name }}, your account has been created!"
Payload:  {"first_name": "Ali"}
Result:   "Hello Ali, your account has been created!"
```

## User Preferences

Before sending, the service checks if the user has enabled that channel:

- Preference `is_enabled=False` → notification blocked
- Preference `is_enabled=True` → notification sent
- No preference found → notification sent (default: enabled)

## Access Control

| Endpoint | Access |
|----------|--------|
| `/register/`, `/login/` | Public |
| `/channels/`, `/templates/`, `/preferences/` | Authenticated users |
| `/notifications/` (GET) | Authenticated users (own only) |
| `/notifications/send/` | Admin only |
| `/notifications/stats/` | Admin only |