import os
from datetime import timedelta
from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or 'your-secret-key-fallback'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    SESSION_PERMANENT = False

    MAIL_SERVER = os.getenv("MAIL_SERVER") or 'smtp.googlemail.com'
    MAIL_PORT = int(os.getenv("MAIL_PORT") or 587)
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS").lower() == 'true' if os.getenv("MAIL_USE_TLS") else False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER") or 'quotesapp3@gmail.com'

    CELERY = dict(
        broker_url="redis://redis:6379/0",
        result_backend="redis://redis:6379/0",
        timezone="Europe/Warsaw",
        enable_utc=False,

        beat_schedule={
            'add-every-30-seconds': {
                'task': 'app.tasks.schedule_daily_quotes',
                'schedule': crontab(minute='*/1')
            },
        }
    )