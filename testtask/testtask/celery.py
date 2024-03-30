import os
import sys


from celery import Celery


sys.path.append("../../main")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testtask.settings')

app = Celery('testtask')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')