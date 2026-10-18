# Task Manager API Documentation

## Base path

/api/

For local development: http://127.0.0.1:8000/api/
For Codespaces: use the forwarded port-8000 URL followed by /api/.

## Authentication

None in this development prototype. Keep Codespaces port visibility private.

## Request format

Content-Type: application/json

All resource paths end with a slash.
Responses are JSON except successful DELETE responses, which have no body.

## Create a task

POST /api/tasks/

```json
{
  "title": "Complete backend assignment",
  "description": "Build and test the REST API.",
  "status": "todo",
  "due_date": null
}
```

Returns 201 with the created task object, including its generated ID and
creation/modification timestamps.

## List tasks

GET /api/tasks/

Returns 200 with an array, ordered newest first. Empty result: [].

## Retrieve a task

GET /api/tasks/{id}/

Returns 200 with a task object, or 404 if not found.

## Replace editable fields

PUT /api/tasks/{id}/

Supply title, description, status, and due_date.
Returns 200 with the updated object.
Title is required; optional omitted fields are not guaranteed to reset.
Use PATCH for intentional partial updates.

## Partially update a task

PATCH /api/tasks/{id}/

```json
{
  "status": "done"
}
```

Returns 200 with the updated task.

## Delete a task

DELETE /api/tasks/{id}/

Returns 204 with no response body, or 404 if not found.

## Validation

- title: 3-150 characters after trimming; required on creation
- description: optional string; may be empty
- status: todo, in_progress, or done
- due_date: valid YYYY-MM-DD date or null
- id, created_at, updated_at: read-only; input values are ignored

## Error responses

| Status | Meaning |
|---|---|
| 400 | Invalid input or malformed JSON |
| 404 | Task not found |
| 405 | Method not allowed |
| 415 | Unsupported request content type |
| 500 | Unexpected server error |

API view exception example:

```json
{
  "error": {
    "status_code": 400,
    "details": {
      "title": [
        "Title must contain at least 3 characters."
      ]
    }
  }
}
```

Unknown URLs outside the API views may use Django's default error responses.

## Interactive and machine-readable documentation

- /api/docs/
- /api/redoc/
- /api/schema/
- openapi.yaml in the repository
