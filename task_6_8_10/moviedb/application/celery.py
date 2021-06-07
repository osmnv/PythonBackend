
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE','application.settings')
app = Celery('application')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'simple_task': {
        'task': 'movies.tasks.simple_task',
        'schedule': 5,
    },
}