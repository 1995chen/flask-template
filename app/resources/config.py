# -*- coding: utf-8 -*-


import inject
import template_logging
from flask import Blueprint
from flask_restful import Resource, reqparse
from typing import Any

from app.resources import Api
from app.dependencies import Config, bind

logger = template_logging.getLogger(__name__)
config: Config = inject.instance(Config)


class Config(Resource):
    # http://www.pythondoc.com/Flask-RESTful/reqparse.html

    # 这里是公共参数定义
    common_parser = reqparse.RequestParser()

    def get(self) -> Any:
        """
        获取用户登陆信息
        """
        # [继承公共参数]
        get_parser = self.common_parser.copy()
        get_parser.add_argument('inner_call_uuid', type=str, default='', required=True)
        # 拿到本次请求数据[这里会拿到所有数据]
        args = get_parser.parse_args()
        logger.info(f"args is {args}")
        # 验证内部调用UID
        if args['inner_call_uuid'] != config.INNER_CALL_UID:
            return {
                'status': 'invalid inner_call_uid'
            }
        # 刷新配置
        inject.clear_and_configure(bind, bind_in_runtime=False)
        return {
            'status': 'success'
        }


def get_resources():
    blueprint = Blueprint('Config', __name__)
    api = Api(blueprint)
    api.add_resource(Config, '/refresh')
    return blueprint
