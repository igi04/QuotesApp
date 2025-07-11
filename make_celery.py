from app import create_app
from app.tasks import schedule_daily_quotes

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
