# 📝 Microblog

A simple blogging web application where users can create posts, view other users’ posts, and interact in a basic social feed. Users can register, log in, and manage their content.  

> **💡 Note:** This project is a learning exercise following a Flask tutorial to practice building web applications. It demonstrates core Flask concepts such as routing, templates, forms, authentication, database models, and session management. It is intended for educational purposes

> **⚠️ Limitations:** Flask-Mail has not yet been fully configured. 

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
- **flask-babel** - Language support 

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
### Create Python environment
```
python -m venv venv
source venv/bin/activate // activate environment
deactivate               // exit envionrment
```

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

### Translation Files
---
```
pybabel extract -F babel.cfg -k _l -o messages.pot .
```
- pybabel extract command reads the configuration file given in the -F option, then scans all the code and template files in the directories that match the configured sources, starting from the directory given in the command (the current directory or . in this case)
- By default, pybabel will look for _() as a text marker, but I have also used the lazy version, which I imported as _l(), so I need to tell the tool to look for those too with the -k _l
- The -o option provides the name of the output file.
```
pybabel init -i messages.pot -d app/translations -l zh 
``` 
Starts the process of creating a translation for each language that is to be supported in addition to the base one (in this case chinese)

- The pybabel init command takes the messages.pot file as input and writes a new language catalog to the directory given in the -d option for the language specified in the -l option. I'm going to be installing all the translations in the app/translations directory, because that is where Flask-Babel will expect translation files to be by default. 
- The command will create a zh subdirectory inside this directory for the chinese data files. In particular, there will be a new file named app/translations/zh/LC_MESSAGES/messages.po, that is where the translations need to be made.

- If you want to support other languages, just repeat the above command with each of the language codes you want, so that each language gets its own repository with a messages.po file.

- This messages.po file that created in each language repository uses a format that is a standard for language translations, the format used by the `gettext` utility. 

To generate a new language without the complexity of the above code run:
```
flask translate init <language-code>
```

To compile:
```
pybabel compile -d app/translations

# Shortened to (in app/cli):
flask translate compile 
```

If you missed some text, wrap them with `_()` or `_l()` then
```
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations


# shortened to (in app/cli):
flask translate update
```
- extract command generates a new version of messages.pot with the previous texts and anything you just wrapped
update command merges the new messages.pot file and messages.po

# ▶️ Run the Application
```
python3 -m flask run
```

