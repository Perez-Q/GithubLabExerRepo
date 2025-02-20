from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(): 
    app = Flask(__name__) # initialize the app
    app.config['SECRET_KEY'] = 'amongus' # secret admin key wooo
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # sql database is located at ///
    db.init_app(app)

    from .views import views #Relative import {.}
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/') # Registers the blueprint of views with the route of /
    app.register_blueprint(auth, url_prefix ='/') #  Registers the blueprint of AUTH with the route of /
    
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id): #Loads the user from primary key
        return User.query.get(int(id))

    return app


def create_database(app): #Check if database exist if exist nice
    if not os.path.exists('Website/' + DB_NAME): #the checker
        with app.app_context():
            db.create_all() #This creates the database
        print('Created Database!')