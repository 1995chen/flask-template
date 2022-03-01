# -*- coding: utf-8 -*-


from typing import Dict, Any

import inject
import template_logging
from template_apollo import ApolloClient

from app.dependencies import bind

logger = template_logging.getLogger(__name__)


def config_changed_handler(entry: Dict[str, Any]) -> Any:
    logger.info(f"get entry: {entry}")
    # 获取阿波罗实例
    apollo_client: ApolloClient = inject.instance(ApolloClient)
    # 重新绑定配置
    inject.clear_and_configure(bind, bind_in_runtime=False)
    # 立即获取apollo实例
    inject.instance(ApolloClient)
    # 停止当前线程
    apollo_client.stop()
