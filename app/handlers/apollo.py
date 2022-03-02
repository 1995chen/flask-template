# -*- coding: utf-8 -*-


from typing import Dict, Any

import template_logging
from template_apollo import ApolloClient

from app.dependencies import bind, Config, inject

logger = template_logging.getLogger(__name__)


def config_changed_handler(entry: Dict[str, Any]) -> Any:
    logger.debug(f"get entry: {entry}")
    old_config: Config = inject.instance(Config)
    # 获取阿波罗实例
    old_apollo_client: ApolloClient = inject.instance(ApolloClient)
    # 重新绑定配置
    inject.clear_and_configure(bind, bind_in_runtime=False)
    # 立即获取apollo实例
    new_apollo_client: ApolloClient = inject.instance(ApolloClient)
    new_config: Config = inject.instance(Config)
    logger.error(
        f"old_config-{id(old_config)} is {old_config}\n"
        f"new_config-{id(new_config)} is {new_config}\n"
        f"old_apollo_client-{id(old_apollo_client)} is {old_apollo_client}\n"
        f"new_apollo_client-{id(new_apollo_client)} is {new_apollo_client}\n"
    )
    # 停止当前线程
    old_apollo_client.stop()
