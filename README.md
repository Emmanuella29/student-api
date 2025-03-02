# Student API

## Overview
This is a Flask-based **Student API** that allows users to **Create, Read, Update, and Delete (CRUD)** student records stored in a PostgreSQL database. The API follows RESTful principles and includes features like database migrations, environment variable configurations, and API documentation.

## Features
- **Create, Retrieve, Update, and Delete** student records.
- **PostgreSQL integration** with Flask SQLAlchemy.
- **Flask-Migrate** for database version control.
- **Environment variable support** using `dotenv`.
- **API testing with Postman**.
- **GitHub repository for version control**.

## Technologies Used
- **Python 3.12**
- **Flask 3.1.0**
- **Flask-SQLAlchemy**
- **Flask-Migrate (Alembic)**
- **PostgreSQL**
- **Postman** (for API testing)
- **Git & GitHub** (for version control)

## Project Structure
```
student-api/
│── api/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│── instance/
│── migrations/
│── tests/
│   ├── test_routes.py
│── .gitignore
│── .env
│── app.py
│── config.py
│── wsgi.py
│── Makefile
│── README.md
│── requirements.txt
```

## Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Emmanuella29/student-api.git
cd student-api
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the project root and add:
```
DATABASE_URL=postgresql://postgres:myella@localhost/student-api
FLASK_APP=app.py
FLASK_ENV=development
```

### 5️⃣ Initialize the Database
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6️⃣ Run the Flask Application
```sh
flask run
```
Access the API at: **http://127.0.0.1:5000**

## API Endpoints
| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | /students           | Retrieve all students |
| GET    | /students/{id}      | Get a specific student |
| POST   | /students           | Add a new student |
| PUT    | /students/{id}      | Update student details |
| DELETE | /students/{id}      | Remove a student |

## Testing with Postman
1. Open **Postman**.
2. Set the request **URL** as `http://127.0.0.1:5000/students`.
3. Use the appropriate **HTTP method** (GET, POST, PUT, DELETE).
4. For **POST/PUT**, set `Content-Type: application/json` in Headers and provide a JSON body.

Example JSON for adding a student:
```json
{
    "name": "John Doe",
    "age": 22,
    "course": "Computer Science"
}
```

## Pushing Updates to GitHub
After making changes, commit and push:
```sh
git add .
git commit -m "Updated API features"
git push origin main
```

## License
This project is licensed under the **MIT License**.

 
