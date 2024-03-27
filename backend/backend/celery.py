import os

from celery import Celery

from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# app.conf.beat_schedule = {
#     "status_check": {
#         "task": "sitedb.Tasks.PeriodicTasks.status_check.py",
#         "schedule": crontab(minute="*"),  # hour="*/6"
#     },
# }
