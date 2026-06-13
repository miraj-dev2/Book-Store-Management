# Book-Store-Management
RESTful Book Store API built with FastAPI and Pydantic
#  Book Store API

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A lightweight, production-ready RESTful API for managing a book store — built with **FastAPI** and **Pydantic v2**. Supports full CRUD operations, author-based filtering, and proper HTTP semantics.

---

##  Features

-  Full CRUD — Create, Read, Update, Delete books
- Filter books by author name (case-insensitive)
-  Partial updates — only send the fields you want to change
-  Input validation via Pydantic v2
-  Auto-generated interactive API docs (Swagger UI & ReDoc)
-  Proper HTTP status codes (`201`, `204`, `404`)

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| FastAPI | Web framework |
| Pydantic v2 | Data validation & serialization |
| Uvicorn | ASGI server |

---

##  Project Structure

```
book-store-api/
├── main.py            # All routes and business logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Git ignored files
└── README.md          # Project documentation
```

---

##  Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/miraj-dev2/Book-Store-Management.git
cd Book-Store-Management

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload
```

Server will start at: **`http://127.0.0.1:8000`**

---

## API Documentation

Interactive docs available at:
- **Swagger UI** → `http://127.0.0.1:8000/docs`
- **ReDoc** → `http://127.0.0.1:8000/redoc`

---

## Endpoints

### Books

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| `POST` | `/books` | Create a new book | `201 Created` |
| `GET` | `/books` | Get all books | `200 OK` 
|  GET    |/books?author={name}|Filter books by author|200 OK
| `GET` | `/books/{id}` | Get a single book by ID | `200 OK` |
| `PUT` | `/books/{id}` | Update a book (partial) | `200 OK` |
| `DELETE` | `/books/{id}` | Delete a book | `204 No Content` |

---

## Request & Response Examples

### Create a Book — `POST /books`

**Request Body:**
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 12.99
}
```

**Response — `201 Created`:**
```json
{
  "id": 3,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 12.99
}
```

---

### Get All Books — `GET /books`

**Response — `200 OK`:**
```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "price": 14.99
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "price": 9.99
  }
]
```

---

### Filter by Author — `GET /books?author=tolkien`

**Response — `200 OK`:**
```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "price": 14.99
  }
]
```

---

### Update a Book — `PUT /books/{id}`

Only send the fields you want to update — all fields are optional.

**Request Body:**
```json
{
  "price": 11.49
}
```

**Response — `200 OK`:**
```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "price": 11.49
}
```

---

### Book Not Found — `GET /books/99`

**Response — `404 Not Found`:**
```json
{
  "detail": "Book not found"
}
```

---

##  Notes

> This project uses **in-memory storage** (Python dictionary). All data resets on server restart. A future version will integrate a persistent database (PostgreSQL via SQLAlchemy or SQLModel).

---

##  Roadmap

- [x] Basic CRUD operations
- [x] Author filtering
- [x] Partial updates
- [ ] Persistent database (PostgreSQL)
- [ ] Response models
- [ ] Authentication (JWT)
- [ ] Pagination

---

##  Author

**Miraj Khan**

- GitHub: [@miraj-dev2](https://github.com/miraj-dev2)
-  CSE Student @ East West University, Bangladesh

---

## License

This project is licensed under the [MIT License](LICENSE).

---

