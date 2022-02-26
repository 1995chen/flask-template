# -*- coding: utf-8 -*-


from typing import Dict, Any

import inject
import template_logging

from app.dependencies import Config
from app.constants.auth import Role
from app.exceptions import NoOwnershipException, AuthorizedFailException, UserInfoMissingException

config: Config = inject.instance(Config)
logger = template_logging.getLogger(__name__)


def get_user_roles_handler(user_info: Any):
    logger.info(f"get_user_roles_handler, user_info is {user_info}")
    logger.warning("you may forget to implement handler: get_user_roles_handler")
    return [Role.Leader]


def user_define_validator_handler(user_info: Any, jwt_obj: Dict[str, Any]):
    # 检验jwt token
    if not jwt_obj or not jwt_obj.get('data') or not jwt_obj["data"].get('username'):
        raise AuthorizedFailException()
    # 校验数据的完整性
    if not user_info or not user_info.get('status') or not user_info.get('username'):
        raise UserInfoMissingException()
    if user_info['status'] == 0 or user_info['username'] != jwt_obj["data"]["username"]:
        raise NoOwnershipException()


def get_user_info_handler(jwt_obj: Dict[str, Any]) -> Dict[str, Any]:
    """
        从jwt字典中提取用户信息
    """

    return {
        "username": jwt_obj["data"]["username"]
    }
