# -*- coding: utf-8 -*-


import template_logging

from app.dependencies import bind, inject

logger = template_logging.getLogger(__name__)

inject.configure(dependencies.bind, bind_in_runtime=False)
