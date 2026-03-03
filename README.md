# 📝 Microblog

A simple blogging web application where users can create posts, view other users’ posts, and interact in a basic social feed. Users can register, log in, and manage their content.  

> ** 💡 Note:** This project is a learning exercise following a Flask tutorial to practice building web applications. It demonstrates core Flask concepts such as routing, templates, forms, authentication, database models, and session management. It is intended for educational purposes

> ** ⚠️ Limitations:** Flask-Mail has not yet been fully configured. 

---

## Features
- 👤 User registration and login/logout
- ✍️ Create, edit, and view blog posts
- 📰 Display posts from all users in a feed
- ⏱ Track user activity timestamps using Flask-Moment
- 🔑 Password reset functionality using email and token-based validation

## 📦 Dependencies

### 🖥 Flask & Extensions

- **Flask** – Python web framework for handling requests, routing, sessions, and template rendering (Jinja2).  
- **Flask-SQLAlchemy** – Integrates SQLAlchemy with Flask. Provides `db.Model` and `db.session` to interact with databases in an ORM style. Supports multiple databases, including SQLite for local development.  (ORM is the bridge between OOP and Relational DBs)
- **SQLAlchemy** – The core ORM library. Handles database models, queries, relationships, and transactions.  
- **Flask-Migrate** – Wraps Alembic to provide database migrations for SQLAlchemy. Helps evolve the database schema safely.  
- **Flask-Login** – Manages user authentication. Provides `login_user()`, `logout_user()`, `current_user`, `@login_required`, and `UserMixin`. Uses Flask sessions to persist login state.  
- **Flask-Moment** – Integrates [Moment.js](https://momentjs.com/) into Jinja templates. Simplifies formatting, parsing, and displaying timestamps in different timezones.  
- **Flask-Mail** – Adds email sending capabilities to Flask. Useful for password resets or notifications (note: may require SMTP configuration).  
- **Flask-WTF** – Integrates [WTForms](https://wtforms.readthedocs.io/) with Flask. Adds CSRF protection and helper methods like `validate_on_submit()`.  

### 📝 Form Handling

- **WTForms** – Python library for rendering HTML forms, validating input data, and handling user submissions securely.  

### 🔐 Security & Tokens

- **Werkzeug** – Provides low-level web utilities and secure password hashing. Used internally by Flask.  
- **hashlib** – Python standard library module for hashing (used for token generation, not for password hashing).  
- **PyJWT** – Create, sign, and verify JSON Web Tokens (JWT). Used for password reset tokens or API authentication.  

### 🛠 Utilities & Standard Library

- **datetime** – Track timestamps, token expiration, and user last-seen data.  
- **os** – Read environment variables, file paths, and configuration.  
- **logging** – Log errors, create rotating file handlers, and send notifications via SMTP.  
- **threading** – Run background tasks asynchronously (e.g., sending emails).  
- **time** – Measure durations or create timestamps.  
- **urllib** – Parse and validate URLs (e.g., for redirect safety).  
- **typing** – Provides type hints for better code readability and static analysis.  
- **email** – Python standard library module for constructing and parsing email messages.  

---

## ⚙️ Setup

### 📥 Install dependencies

```bash
pip install -r requirements.txt
```
### 🗄 Initialize database migrations
```
flask db init
```
Whenever you wish to make changes to the models:
```
# generate migration script
flask db migrate -m "<message>"

# apply migration
flask db upgrade

# Rollback (Optional)
flask db downgrade
```

# ▶️ Run the Application
```
python3 -m flask run
```

