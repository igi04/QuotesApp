from flask import Flask, render_template

from .extensions import db,login_manager,mail
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # db.init_app(app)
    # mail.init_app(app)
    # login_manager.init_app(app)

    @app.route('/')
    def hello():
        return render_template("home.html")

    return app