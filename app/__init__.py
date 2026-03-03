from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager # Manages user logged in state. Remembers that the user is logged in and provides the 'remember me' functionality
from flask_moment import Moment
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
from flask_mail import Mail
import os

# wrapping app with libraries creates a context processor which is a function that Flask calls every time a template is to be rendered. And it fills in variables without every being passed (acts like a global variable but only for templates).
# Context processors are specific to Flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
moment = Moment(app) 

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR) # only reports errors not warnings
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


from app import routes, models, errors

'''
flask_sqlalchemy is a wrapper for sql where you can use high level entities such as classes, methods,objects to manage a database instead of using tables and SQL. it handles the conversion for you

flask_migrate is a wrapper for Alembic which is a database migration framework for SQLAlchemy. Used when the existing database needs updates and changed made to it so this framework helps migrate data to a new modified structure
'''
