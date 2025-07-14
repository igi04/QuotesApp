from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from celery import Celery
from flask import Flask

#Init all needed objects
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
celery = Celery()

#Flask integration with Celery (from flask docs)
from celery import Celery, Task
def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
