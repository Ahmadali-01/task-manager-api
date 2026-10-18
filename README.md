# Task Manager REST API

A RESTful backend built with Django REST Framework and SQLite.

## Features

- Create, list, retrieve, replace, partially update, and delete tasks
- Persistent SQLite storage
- Serializer-based input validation
- Structured JSON errors for API view exceptions
- Swagger UI, ReDoc, and exported OpenAPI documentation
- 12 automated API tests

## Requirements

Python 3.10 or newer and the dependencies in requirements.txt.

## Setup in GitHub Codespaces or Linux/macOS

Open this repository in GitHub Codespaces, or clone it locally.
Run each command separately from the repository root:

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver 0.0.0.0:8000
```

In Codespaces, open the Ports tab and open port 8000 in the browser.
Keep the forwarded port private.

For local Windows Command Prompt, activate the environment with
`.venv\Scripts\activate.bat` instead of the source command.

## Endpoints

| Method | Path | Purpose | Success |
|---|---|---|---|
| POST | /api/tasks/ | Create task | 201 |
| GET | /api/tasks/ | List tasks | 200 |
| GET | /api/tasks/{id}/ | Retrieve task | 200 |
| PUT | /api/tasks/{id}/ | Replace editable task fields | 200 |
| PATCH | /api/tasks/{id}/ | Update selected fields | 200 |
| DELETE | /api/tasks/{id}/ | Delete task | 204 |

Use trailing slashes and Content-Type: application/json for request bodies.
The list endpoint returns an unpaginated array.

## Task data model

| Field | Type | Rules |
|---|---|---|
| id | Integer | Auto-generated primary key; read-only |
| title | String | Required on creation; 3-150 trimmed characters |
| description | Text | Optional; default empty string |
| status | String | todo, in_progress, or done; default todo |
| due_date | Date | Optional YYYY-MM-DD date or null |
| created_at | Date/time | Automatically generated; read-only |
| updated_at | Date/time | Automatically maintained; read-only |

For PUT, supply all editable fields for an explicit replacement.
Use PATCH when changing only selected fields.

## Documentation

- /api/docs/ - Interactive Swagger UI
- /api/redoc/ - ReDoc
- /api/schema/ - OpenAPI schema endpoint
- API_DOCUMENTATION.md - Written API documentation
- openapi.yaml - Exported OpenAPI specification

## Tests

```bash
python manage.py test
```

## Regenerate OpenAPI specification

```bash
python manage.py spectacular --file openapi.yaml --validate
```

## Project structure

- config/: project settings and root routes
- tasks/models.py: Task database model
- tasks/serializers.py: validation and serialization
- tasks/views.py: CRUD viewset
- tasks/urls.py: resource routing
- tasks/exceptions.py: JSON API exception handler
- tasks/tests.py: automated API tests
- tasks/migrations/: database migration history

## Security and scope

This is a development assignment prototype, not a production deployment.
API authentication is intentionally disabled and all tasks are shared.
Do not expose the forwarded port publicly.
DEBUG must be disabled and a private SECRET_KEY, authentication,
authorization, and production server configuration must be added before
public deployment.

The SQLite database is not committed. Running migrate recreates its tables.
Migration files must be committed.
