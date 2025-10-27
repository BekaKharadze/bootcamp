import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CELERY_BEAT_SCHEDULE'
, 'Day7.settings')

app = Celery('Day7')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'daily_summary': {
        'task': 'core.tasks.daily_summary',
        'schedule': crontab(hour=0, minute=0),
    },
}