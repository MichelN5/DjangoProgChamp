# ProgChamp Backend

Django REST API for ProgChamp, a coding challenge platform with authentication, profiles, comments, challenge creation, completion tracking, and code checking for Python and C++.

This folder is intended to run as part of the full-stack project from the repository root with Docker Compose.

## Features

- Token-based authentication with Djoser
- Challenge listing, details, search, and category filtering
- User-created challenges
- Completed challenge tracking
- Profile image upload support
- Comments on solution pages
- Python code execution
- C++ code compilation and execution with `g++`
- Seed command for starter Python and C++ challenges

## Tech Stack

- Python 3.10
- Django 3.2
- Django REST Framework
- Djoser
- SQLite for local development
- Pillow
- django-cors-headers
- `g++` inside the Docker image for C++ challenges

## Docker Usage

From the project root:

```bash
docker compose up --build
```

The backend runs at:

```text
http://127.0.0.1:8000/
```

The backend container runs migrations and seeds starter challenges automatically.

## Local Setup

Use this only if you want to run the backend without Docker.

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Run migrations and seed starter data:

```bash
python manage.py migrate
python manage.py seed_challenges
```

Start the server:

```bash
python manage.py runserver
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | Enables debug mode when set to `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts |
| `CORS_ALLOWED_ORIGINS` | Comma-separated frontend origins |

## Useful Commands

```bash
python manage.py migrate
python manage.py seed_challenges
python manage.py createsuperuser
python manage.py runserver
```

Seeded development admin:

```text
username: seed_admin
password: admin12345
```

## Main API Routes

| Method | Route | Purpose |
|---|---|---|
| `GET` | `/challenges/` | List all challenges |
| `GET` | `/challenges/?category=python` | List Python challenges |
| `GET` | `/challenges/?category=cpp` | List C++ challenges |
| `GET` | `/challenges/<category_slug>/<challenge_slug>/` | Challenge details |
| `POST` | `/run-code/` | Run submitted Python or C++ code |
| `GET` | `/usercomch/` | Current user's completed challenges |
| `GET` | `/usercrch/` | Current user's created challenges |
| `POST` | `/completedchallenges/` | Mark a challenge as completed |
| `POST` | `/create/` | Create a challenge |
| `GET` | `/comments/<challenge_id>/` | Get challenge comments |
| `POST` | `/comments/create` | Create a comment |
| `POST` | `/api/token/login/` | Token login |

## Project Structure

```text
DjangoProgChamp/
  Challenges/       # Challenge models, serializers, views, routes, seed command
  UserProfile/      # Profile models, serializers, views, routes
  comments/         # Comment models, serializers, views, routes
  ProgChamp/        # Django settings and root URL configuration
  Dockerfile
  manage.py
  requirements.txt
```

## Repository Hygiene

Ignored local/generated files include:

- `.venv/`
- `db.sqlite3`
- `media/`
- `static/`
- `staticfiles/`
- `wheelhouse/`
- `__pycache__/`
- `*.log`
- `.env`
