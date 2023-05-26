import os

from kombu import Queue

# Rabbitmq Broker setting

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_ACKS_LATE = True  # messages will be acknowledged after the task has been executed, not just before
CELERY_TASK_REJECT_ON_WORKER_LOST = True  # Enabling this can cause message loops; make sure you know what you’re doing.

CELERY_TASK_TIME_LIMIT = 60 * 5
CELERY_TASK_SOFT_TIME_LIMIT = 60


# CELERY_IMPORTS # use this to include task outside the default path


class CeleryTasks:
    pass


class CeleryQueues:
    DEFAULT = "default"  # queue for all other tasks (low-priority background tasks)

    @classmethod
    def as_list(cls):
        return [cls.DEFAULT]


CELERY_TASK_QUEUES = [Queue(queue) for queue in CeleryQueues.as_list()]

CELERY_TASK_DEFAULT_QUEUE = CeleryQueues.DEFAULT
CELERY_TASK_DEFAULT_EXCHANGE = "default"
CELERY_TASK_DEFAULT_ROUTING_KEY = "default"
CELERY_TASK_CREATE_MISSING_QUEUES = False

CELERY_TASK_ROUTES = {}

CELERY_BEAT_SCHEDULE = {}
