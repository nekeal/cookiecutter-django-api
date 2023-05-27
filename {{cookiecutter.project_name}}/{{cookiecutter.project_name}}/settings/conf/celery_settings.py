import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_ACKS_LATE = True  # messages will be acknowledged after the task has been executed, not just before
CELERY_TASK_REJECT_ON_WORKER_LOST = True  # Enabling this can cause message loops; make sure you know what you’re doing.

CELERY_TASK_TIME_LIMIT = 60 * 5
CELERY_TASK_SOFT_TIME_LIMIT = 60
