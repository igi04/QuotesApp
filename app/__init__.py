from flask import Flask
from .extensions import db, migrate
from .models import User, Quote, likes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # mail.init_app(app)
    # login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .quotes import quotes as quotes_blueprint
    app.register_blueprint(quotes_blueprint)

    return app