# User Registration and Authentication System Using Flask and SQLite

## 📌 Project Overview

This project is a **User Registration and Authentication System** built using **Python Flask** and **SQLite database**.

* Users can create an account and securely store their credentials.
* Passwords are hashed before storing them in the database.
* Users can log in and access protected pages using session management.
* The project demonstrates Flask routing, form handling, database operations, and authentication flow.


---

# 🚀 Features

## 1. User Registration

* Users can create a new account using a username and password.
* User details are stored in an SQLite database.
* Duplicate usernames are prevented using database constraints.
* Passwords are securely hashed before storing them in the database.

---

## 2. User Login Authentication

* Registered users can log in using their credentials.
* The system verifies the entered password against the stored password hash.
* Invalid credentials are rejected.
* Successful login creates an authenticated session.

---

## 3. Session Management

* User sessions are maintained using Flask sessions.
* Protected pages can only be accessed by authenticated users.
* Unauthorized users are redirected to the login page.

---

## 4. Secure Password Storage

Instead of storing plain-text passwords, this project uses password hashing.

Example:

Before hashing:

```
mypassword123
```

Stored in database:

```
scrypt:32768:8:1$xxxxxxxxxxxxxxxx
```

Technologies used:

* `generate_password_hash()`
* `check_password_hash()`

from Werkzeug security module.

---

## 5. Database Integration

The project uses SQLite for storing user information.

Database table:

### auth_users

| Column   | Description            |
| -------- | ---------------------- |
| id       | Unique user identifier |
| username | User's unique username |
| password | Hashed password        |

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask Framework
* SQLite Database

## Frontend

* HTML5
* Jinja2 Templates

## Security

* Werkzeug Password Hashing
* Flask Sessions

## Development Tools

* Git
* GitHub
* Virtual Environment

---

# 📂 Project Structure

---

# ⚙️ How It Works

## Registration Flow

```
User enters details
        |
        ↓
Flask receives POST request
        |
        ↓
Validate user input
        |
        ↓
Hash password
        |
        ↓
Store user in SQLite database
        |
        ↓
Registration completed
```

---

## Login Flow

```
User enters username/password
        |
        ↓
Flask receives login request
        |
        ↓
Search user in database
        |
        ↓
Compare password hash
        |
        ↓
Create user session
        |
        ↓
Redirect to dashboard
```

---

# 🖥️ Installation and Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python app.py
```

Application runs at:

```
http://127.0.0.1:5000
```

---

# 📚 Concepts Learned

This project helped me understand:

* Flask application structure
* URL routing
* GET and POST requests
* HTML form handling
* Database connectivity
* SQL queries using Python
* User authentication workflow
* Session management
* Password hashing
* Template rendering using Jinja2
* Git version control

---

# 🔮 Future Improvements

Possible enhancements:

* Email verification
* Forgot password functionality
* OTP authentication
* Role-based authentication (Admin/User)
* PostgreSQL database integration
* REST API implementation
* JWT authentication
* Deployment using cloud platforms

---

# 👨‍💻 Author

Rahul Ravi
