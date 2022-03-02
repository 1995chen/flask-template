# -*- coding: utf-8 -*-


import template_logging
from celery import Celery

from app.dependencies import inject

logger = template_logging.getLogger(__name__)

celery_app: Celery = inject.instance(Celery)


@celery_app.task(ignore_result=True, time_limit=600)
def do_test():
    logger.info(f'run do_test done')
