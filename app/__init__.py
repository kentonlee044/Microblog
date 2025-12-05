from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager # Manages user logged in state. Remembers that the user is logged in and provides the 'remember me' functionality

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

'''
flask_sqlalchemy is a wrapper for sql where you can use high level entities such as classes, methods,objects to manage a database instead of using tables and SQL. it handles the conversion for you

flask_migrate is a wrapper for Alembic which is a database migration framework for SQLAlchemy. Used when the existing database needs updates and changed made to it so this framework helps migrate data to a new modified structure
'''
