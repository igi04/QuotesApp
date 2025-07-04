from flask import Flask, render_template

from .extensions import db,login_manager,mail
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # db.init_app(app)
    # mail.init_app(app)
    # login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .quotes import quotes as quotes_blueprint
    app.register_blueprint(quotes_blueprint)

    return app