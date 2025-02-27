from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'amongus'  
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import User, Note, HybridCar, FuelUsage  # ✅ Import models first
    create_database(app)  # ✅ Initialize database before blueprints

    from .views import views  # ✅ Now import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')  
    app.register_blueprint(auth, url_prefix='/')  

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):  
        return User.query.get(int(id))

    return app

def create_database(app):  
    if not os.path.exists('Website/' + DB_NAME):  
        with app.app_context():
            db.create_all()  
        print('Created Database!')
