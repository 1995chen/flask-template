# -*- coding: utf-8 -*-


from typing import Dict, Any

import inject
import requests
import template_logging
from template_apollo import ApolloClient

from app.dependencies import bind, Config

logger = template_logging.getLogger(__name__)


def config_changed_handler(entry: Dict[str, Any]) -> Any:
    logger.info(f"get entry: {entry}")
    # 通知API刷新配置
    # noinspection PyBroadException
    try:
        # 通知API刷新配置
        requests.get(f"http://127.0.0.1:{Config.PORT}/api/v1/config/refresh?inner_call_uuid={Config.INNER_CALL_UID}")
        inject.clear_and_configure(bind, bind_in_runtime=False)
        # 获取阿波罗实例[停止线程]
        apollo_client: ApolloClient = inject.instance(ApolloClient)
        # 停止当前线程
        apollo_client.stop()
    except Exception:
        logger.warning(f"failed to refresh config", exc_info=True)
