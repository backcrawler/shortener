from celery.task import periodic_task
from celery.utils.log import get_task_logger

from datetime import timedelta, datetime

from .models import Link

logger = get_task_logger(__name__)


@periodic_task(run_every=timedelta(days=1), name='clean')
def clean_outdated():
    """
    Cleans old short urls
    """
    outdated_links = Link.objects.filter(date_created__lt=...)  #TODO: fix it
    outdated_links.delete()
    logger.info("Cleaning executed")
