from flask import Flask, render_template
from celery import Celery
from flask_restful import Api


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)
    app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
    celery = make_celery(app)

    return app, celery

app, celery = create_app()
api = Api(app)

from . import views
