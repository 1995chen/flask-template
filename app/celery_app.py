# -*- coding: utf-8 -*-


import template_logging
from celery import Celery

from app.dependencies import inject

logger = template_logging.getLogger(__name__)
celery_app = inject.instance(Celery)
