from celery import shared_task
import subprocess


@shared_task
def update_at_time():
    subprocess.run(["python", "manage.py", "update_db"])