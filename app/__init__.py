from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.views import configure_views

db = SQLAlchemy()
csrf = CSRFProtect()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    configure_views(app)

    from app.auth.views import auth_bp
    app.register_blueprint(auth_bp)

    from app.reviews.views import reviews_bp
    app.register_blueprint(reviews_bp)

    from app.post.views import post_bp
    app.register_blueprint(post_bp)

    return app

from app import views