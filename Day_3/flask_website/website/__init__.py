'''Initiliztion of the web application'''
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Assign a SQLAlchemy object to a var to create the database
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    '''Create the application'''
    app = Flask(__name__) # Because this is called from another file, this will return this files name. In this case it would be "website".
    app.config['SECRET_KEY'] = 'ct5501'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .veiws import veiws
    from .auth import auth
    from .models import User

    app.register_blueprint(veiws, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    #keeps session data
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    '''Create database if it does not exist.'''
    if not path.exists('websit/' + DB_NAME):
        db.create_all(app=app)
