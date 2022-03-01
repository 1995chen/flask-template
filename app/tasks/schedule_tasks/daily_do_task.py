# -*- coding: utf-8 -*-


import inject
import template_logging
from celery import Celery

logger = template_logging.getLogger(__name__)
celery_app: Celery = inject.instance(Celery)


@celery_app.task(ignore_result=True, time_limit=600)
def test_scheduler():
    logger.info(f'run test_scheduler done')
