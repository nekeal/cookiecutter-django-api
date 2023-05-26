import logging
import os

from celery import Celery as BaseCelery
from celery.utils.time import timezone as celery_timezone
from django.conf import settings
from django.utils import timezone

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recevent_printing_manager.settings")

logger = logging.getLogger(__name__)


class Celery(BaseCelery):
    @property
    def timezone(self):
        return celery_timezone.get_timezone(settings.TIME_ZONE)

    def now(self):
        return timezone.localtime()


app = Celery("{{cookiecutter.project_name}}")
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix but remember to use only the new settings names
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# NOTE: start celery locally (in order to connect to all the queues):
# celery -A {{cookiecutter.project_name}} worker -E -l INFO
@app.task(bind=True)
def debug_task(self):
    """
    # add to the queue right now
    debug_task.apply_async()

    # if you want to delay the task execution, use datetime.utcnow()
    debug_task.apply_async(eta=datetime.datetime.utcnow() + datetime.timedelta(seconds=10))
    """
    print("Request: {0!r}".format(self.request))
    logger.info("Request: {0!r}".format(self.request))
