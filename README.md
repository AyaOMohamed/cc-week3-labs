# Week 3 Labs — Books API & Courses API

This repository contains two REST API projects developed as part of the Week 3 labs. Both use **FastAPI** to handle HTTP requests and **SQLite** for data storage, with the Courses API also using SQLAlchemy and Pydantic.

The projects demonstrate how to build API endpoints, store and retrieve records, validate incoming data, handle common request errors, and write unit and integration tests.

---

# 1. Books API

## Overview

The Books API provides a simple interface for creating and retrieving book records. Each book contains a title, author, and publication year, along with an ID assigned by the application.

The API uses SQLite as its database backend and FastAPI to process requests and return JSON responses.

### Features

- Create a new book with its title, author, and publication year.
- Retrieve a list of all books.
- Look up an individual book using its ID.
- Return an appropriate error response when a requested book cannot be found.
- Test endpoints interactively using Postman or the automatically generated API documentation.

## API Endpoints

| HTTP Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| `GET` | `/` | Checks that the API is running. | `200 OK` |
| `GET` | `/books` | Returns all stored books. | `200 OK` |
| `POST` | `/books` | Creates a new book. | `201 Created` |
| `GET` | `/books/{id}` | Retrieves a book by its ID. | `200 OK` |
| `GET` | `/books/{id}` | Returns an error if the book does not exist. | `404 Not Found` |

### Example: Create a Book

Send a `POST` request to `/books` with the following JSON body:

```json
{
  "title": "Postman book",
  "author": "Shane Reddy",
  "year": 2020
}
```

A successful request returns `201 Created` and the newly created book, including its assigned ID.

### Example: Retrieve a Book

After creating a book, use its returned ID to retrieve it:

```http
GET /books/1
```

A successful request returns `200 OK` with the matching book.

If the requested book does not exist, the API returns `404 Not Found`, with a response such as:

```json
{
  "detail": "book not found"
}
```

## Running the Books API

### 1. Navigate to the project directory

```bash
cd week3-books-api
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

Once the server is running, the API is available at:

- **Base URL:** `http://127.0.0.1:8000`
- **Interactive documentation:** `http://127.0.0.1:8000/docs`
- **Alternative documentation:** `http://127.0.0.1:8000/redoc`

Use Postman or Swagger UI to send requests and inspect the responses.

---

# 2. Courses API

## Overview

The Courses API expands on the basic API concepts demonstrated in the Books API. It provides endpoints for creating courses and retrieving course information, with additional handling for duplicate course codes and invalid requests.

The project uses **SQLAlchemy** to represent courses and interact with the database, while **Pydantic** validates request data and defines the expected API data structures.

### Features

- Create a course using its code, title, and lecturer.
- Retrieve all courses stored in the database.
- Retrieve an individual course by its ID.
- Reject requests that omit required fields.
- Prevent duplicate course codes.
- Return appropriate HTTP status codes for successful requests and errors.
- Use SQLAlchemy for database operations.
- Use Pydantic for request validation.
- Run automated tests with pytest to verify API behaviour.

## API Endpoints

| HTTP Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| `GET` | `/` | Checks that the API is running. | `200 OK` |
| `GET` | `/courses` | Returns all stored courses. | `200 OK` |
| `POST` | `/courses` | Creates a new course. | `201 Created` |
| `POST` | `/courses` | Rejects a course with an existing code. | `409 Conflict` |
| `GET` | `/courses/{id}` | Retrieves a course by its ID. | `200 OK` |
| `GET` | `/courses/{id}` | Returns an error if the course does not exist. | `404 Not Found` |

### Example: Create a Course

Send a `POST` request to `/courses` with this JSON body:

```json
{
  "code": "CS101",
  "title": "Computer Science",
  "lecturer": "John Smith"
}
```

If the request succeeds, the API returns `201 Created` and the new course, including its assigned ID.

### Example: Duplicate Course Code

The API does not allow two courses to share the same course code.

Submitting the same course data again should return `409 Conflict`:

```json
{
  "detail": "Course code already exists"
}
```

This demonstrates how the API handles a conflict when a course with the requested code already exists.

### Example: Retrieve a Course

Use the ID returned when creating the course:

```http
GET /courses/1
```

A successful request returns `200 OK` with the matching course.

If the requested course cannot be found, the API returns `404 Not Found`, with a response such as:

```json
{
  "detail": "Course not found"
}
```

### Example: Missing Required Field

The course creation endpoint requires the `code`, `title`, and `lecturer` fields.

If a request omits a required field, FastAPI's request validation should reject it with `422 Unprocessable Entity`.

This behaviour is also covered by the automated tests.

## Running the Courses API

### 1. Create a virtual environment

```bash
python3 -m venv .venv
```

### 2. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Start the development server

```bash
uvicorn main:app --reload
```

The API can then be accessed at:

- **Base URL:** `http://127.0.0.1:8000`
- **Interactive documentation:** `http://127.0.0.1:8000/docs`
- **Alternative documentation:** `http://127.0.0.1:8000/redoc`

Use Postman or Swagger UI to explore the endpoints and test the expected responses.

---

# 3. Automated Testing

The Courses API includes automated tests written with **pytest**. These tests help verify that the API handles valid requests, rejects invalid input, and behaves correctly when database operations fail.

### Test Types

- **Unit Tests — `tests/test_rules.py`**  
  Test individual business rules and validation logic independently, without relying on the full API request-and-response flow.

- **Integration Tests — API tests**  
  Test API endpoints and their interaction with the database, including creating and retrieving records and handling errors.

### Test Isolation

Each API integration test opens its **own independent database session** and uses an isolated database setup. This ensures that:

- Tests do not depend on data created by other tests.
- Database changes from one test do not affect another test.
- Tests can run in any order without relying on shared state.
- Each test produces consistent, reliable results.

This isolation helps prevent order-dependent failures and makes the test suite more predictable.

### Run the Tests

Run these commands from the project root:

```bash
# Run unit tests for business rules
python -m pytest tests/test_rules.py -q

# Run the complete test suite
python -m pytest -q

# Run all tests with detailed output
python -m pytest -v
```