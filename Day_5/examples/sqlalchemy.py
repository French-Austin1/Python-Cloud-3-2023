from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME ="sql_example.db"
db = SQLAlchemy()
def run():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    db.init_app(app)
    create_database(app)

def create_database(app):
    '''Create database if it does not exist.'''
    if not path.exists(DB_NAME):
        db.create_all(app=app)
