import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db, cli
from app.models import User, Post

# purely for development purposes. Returns a dictionary ob objects you want pre-imported when you run 'flask shell' so you don't need to import when you enter shell
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}