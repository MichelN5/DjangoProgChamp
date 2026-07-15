# ProgChamps Backend

Django REST API for **ProgChamps**, a programming-challenges platform. The backend manages challenges, user profiles, comments, authentication, user-created challenges, search, and completion tracking.

The related frontend is available in [`MichelN5/ProgChamps`](https://github.com/MichelN5/ProgChamps).

## Features

- List and retrieve programming challenges
- Search challenges
- Create user-submitted challenges
- Track completed challenges
- User registration and token authentication with Djoser
- User profiles
- Comments and community interaction
- Django admin interface

## Tech Stack

- Python 3
- Django 3.2
- Django REST Framework
- Djoser and token authentication
- SQLite for local development
- Pillow for uploaded images
- django-cors-headers

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/MichelN5/DjangoProgChamp.git
cd DjangoProgChamp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

The project reads these variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `CORS_ALLOWED_ORIGINS`

Set them in your shell or load the `.env` file with your preferred environment-management tool.

### 5. Prepare the database

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

The API will normally be available at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Main API Routes

| Method | Route | Purpose |
|---|---|---|
| `GET` | `/challenges/` | List challenges |
| `GET` | `/challenges/<category_slug>/<product_slug>/` | Retrieve challenge details |
| `GET` | `/challenges/<id>/` | Retrieve a challenge by ID |
| `GET/POST` | `/completedchallenges/` | Work with completed challenges |
| `GET` | `/usercomch/` | List the current user's completed challenges |
| `GET` | `/usercrch/` | List user-created challenges |
| `POST` | `/create/` | Create a challenge |
| `GET` | `/search/` | Search challenges |
| Various | `/api/` | Djoser authentication routes |

Additional profile and comment routes are registered by the `UserProfile` and `comments` applications.

## Project Structure

```text
DjangoProgChamp/
├── Challenges/       # Challenge models, serializers, views, and routes
├── UserProfile/      # User profile functionality
├── comments/         # Comment functionality
├── ProgChamp/        # Main settings and URL configuration
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

## Security and Repository Hygiene

- Secrets and deployment configuration are read from environment variables.
- The local SQLite database is not tracked.
- Uploaded media and generated static output are ignored.
- Production deployments should use a strong secret key, `DEBUG=False`, explicit allowed hosts and CORS origins, and appropriate persistent media/database services.

## Author

Developed by [Michel Naouss](https://github.com/MichelN5).
