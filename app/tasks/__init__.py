# -*- coding: utf-8 -*-


import inject

import template_logging
from celery.signals import task_postrun
from celery import Celery
from kombu import Exchange, Queue

from app.dependencies import Config

logger = template_logging.getLogger(__name__)


@inject.autoparams()
def init_celery(config: Config):
    task_root = 'app.tasks'
    _celery = Celery(
        config.PROJECT_NAME,
        include=[
            'app.tasks.test_task',
            'app.tasks.schedule_task',
        ]
    )
    # 定时任务
    beat_schedule = {
        'schedule_task.test_scheduler': {
            'task': 'app.tasks.schedule_task.test_scheduler',
            'args': (),
            'schedule': 5,
            'options': {
                # 该定时任务会被调度到这个队列
                'queue': f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-beat-queue'
            }
        },
    }

    logger.info(f'Scheduled tasks: {beat_schedule}')
    _celery.conf.update(
        CELERYBEAT_SCHEDULE=beat_schedule,
        # 定义队列[如果需要额外的队列,定义在这里]
        CELERY_QUEUES=[
            # 该默认队列可以不用定义,这里定义作为Example
            Queue(
                f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-queue',
                Exchange(f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-exchange'),
                routing_key=f'{config.PROJECT_NAME}-routing'
            ),
        ],
        # 定义路由[部分任务需要单独的队列处理用于提速,定义在这里]
        CELERY_ROUTES={
            # 该任务可以不用定义,这里定义作为Example
            f'{task_root}.test_task.do_test': {
                'queue': f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-queue',
                'routing_key': f'{config.PROJECT_NAME}-routing'
            },
        },
        # 默认队列
        CELERY_DEFAULT_QUEUE=f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-queue',
        # 默认交换机
        CELERY_DEFAULT_EXCHANGE=f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-exchange',
        # 默认路由
        CELERY_DEFAULT_ROUTING_KEY=f'{config.PROJECT_NAME}-{config.RUNTIME_ENV}-routing',
        CELERY_DEFAULT_EXCHANGE_TYPE='direct',

        BROKER_URL=config.CELERY_BROKER,
        CELERY_RESULT_BACKEND=config.CELERY_BACKEND,
        # 任务的硬超时时间
        CELERYD_TASK_TIME_LIMIT=300,
        CELERY_ACKS_LATE=True,
        CELERY_RESULT_PERSISTENT=False,
        CELERY_TASK_RESULT_EXPIRES=86400,
        CELERY_TASK_SERIALIZER='json',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_RESULT_SERIALIZER='json',
        CELERY_TIMEZONE='Asia/Shanghai',
        CELERY_ENABLE_UTC=True,
        BROKER_CONNECTION_TIMEOUT=10,
        # 拦截根日志配置
        CELERYD_HIJACK_ROOT_LOGGER=False,
        CELERYD_LOG_FORMAT='[%(name)s]:%(asctime)s:%(filename)s:%(lineno)d %(levelname)s/%(processName)s %(message)s',
        # REDBEAT_REDIS_URL 多实例允许celery beat
        redbeat_redis_url=config.REDBEAT_REDIS_URL or config.CELERY_BROKER,
        # 锁前缀
        redbeat_key_prefix=f"{config.PROJECT_NAME}-{config.RUNTIME_ENV}-redbeat",
        # 锁超时时间
        redbeat_lock_timeout=config.REDBEAT_LOCK_TIMEOUT
    )
    return _celery


@task_postrun.connect()
def task_postrun_handler(*args, **kwargs):
    from app.dependencies import MainDBSession
    del args, kwargs
    inject.instance(MainDBSession).remove()
