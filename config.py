import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # loads key if found otherwise gives default value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')