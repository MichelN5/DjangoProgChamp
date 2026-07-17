# ProgChamp Frontend

Vue frontend for ProgChamp, a full-stack coding challenge platform. The app lets users browse Python and C++ challenges, write and check solutions, view official solutions, comment, create challenges, and manage their profile.

This folder is intended to run as part of the full-stack project from the repository root with Docker Compose.

## Features

- Challenge browsing by category
- Challenge details page
- Embedded code editor
- Python and C++ solution checking through the backend API
- Solution and comments page
- User login/signup
- Profile page with completed and created challenges
- Challenge creation form
- Search

## Tech Stack

- Vue 3
- Vue Router
- Vuex
- Axios
- Bootstrap 5
- Ace editor assets

## Docker Usage

From the project root:

```bash
docker compose up --build
```

The frontend runs at:

```text
http://127.0.0.1:8080/
```

The Docker Compose file sets:

```text
VUE_APP_API_BASE_URL=http://127.0.0.1:8000/
```

## Local Setup

Use this only if you want to run the frontend without Docker.

Install dependencies:

```bash
npm install
```

Create a local environment file:

```bash
cp .env.example .env.local
```

Start the dev server:

```bash
npm run serve
```

Build for production:

```bash
npm run build
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `VUE_APP_API_BASE_URL` | Backend API base URL |

Example:

```text
VUE_APP_API_BASE_URL=http://127.0.0.1:8000/
```

## Project Structure

```text
vue-progchamp/
  public/
  src/
    assets/       # Images and editor assets
    components/   # Shared Vue components
    router/       # Vue Router configuration
    store/        # Vuex store
    views/        # Page views
  Dockerfile
  package.json
```

## Repository Hygiene

Ignored local/generated files include:

- `node_modules/`
- `dist/`
- local `.env` files
- logs
- editor/OS files
