# -*- coding: utf-8 -*-


# 客户端错误
from app.exceptions.base import ClientException
from app.constants.code_map import CODE_MAP


class ParamsTypeErrorException(ClientException):
    """参数格式错误"""

    def __init__(self, name, param_type):
        super().__init__()
        self.code = 40001
        self.message = str(CODE_MAP[self.code]) % (name, param_type)


class EnumInvalidException(ClientException):
    """不合法的枚举类型"""

    def __init__(self, name, enum_list):
        super().__init__()
        self.code = 40002
        if isinstance(enum_list, list):
            enum_str = ', '.join([str(o) for o in enum_list])
        else:
            enum_str = enum_list
        self.message = str(CODE_MAP[self.code]) % (name, enum_str)


class JsonInvalidException(ClientException):
    """不合法的json字符串"""

    def __init__(self):
        super().__init__()
        self.code = 40003
        self.message = CODE_MAP[self.code]


class ParamsInvalidException(ClientException):
    """不合法的参数"""

    def __init__(self, errors):
        super().__init__()
        self.code = 40004
        error_text = ''
        for key, value in errors.items():
            error_text += '%s: %s;' % (key, value)
        self.message = str(CODE_MAP[self.code]) % error_text


class RecordExistException(ClientException):
    """记录已存在"""

    def __init__(self):
        super().__init__()
        self.code = 40005
        self.message = CODE_MAP[self.code]


class DumplicateKeyException(ClientException):
    """关键值重复"""

    def __init__(self, name):
        super().__init__()
        self.code = 40007
        self.message = str(CODE_MAP[self.code]) % name


class InvalidRegexException(ClientException):
    """输入不符合正则规则"""

    def __init__(self, name, rule):
        super().__init__()
        self.code = 40008
        self.message = str(CODE_MAP[self.code]) % (name, rule)


class FlowDealedException(ClientException):
    """流程已被审核"""

    def __init__(self):
        super().__init__()
        self.code = 40009
        self.message = CODE_MAP[self.code]


class KeyParamsMissingException(ClientException):
    """缺少必要参数"""

    def __init__(self, name):
        super().__init__()
        self.code = 40010
        self.message = str(CODE_MAP[self.code]) % name


class DbConnectionFailedException(ClientException):
    """数据库连接失败"""

    def __init__(self, msg):
        super().__init__()
        self.code = 40012
        self.message = str(CODE_MAP[self.code]) % msg


class RecordNotFoundException(ClientException):
    """记录不存在"""

    def __init__(self, message=''):
        super().__init__()
        self.code = 40013
        self.message = message or CODE_MAP[self.code]


class UnauthorizedException(ClientException):
    """未登录"""

    def __init__(self):
        super().__init__()
        self.code = 40100
        self.message = CODE_MAP[self.code]


class UserInfoMissingException(ClientException):
    """未找到用户信息"""

    def __init__(self):
        super().__init__()
        self.code = 40101
        self.message = CODE_MAP[self.code]


class NoOwnershipException(ClientException):
    """无编辑权限"""

    def __init__(self):
        super().__init__()
        self.code = 40103
        self.message = CODE_MAP[self.code]


class EleteSendLogException(ClientException):
    """打点发送失败"""

    def __init__(self):
        super().__init__()
        self.code = 40404
        self.message = CODE_MAP[self.code]


class AuthorizedFailException(ClientException):
    """身份验证失败"""

    def __init__(self):
        super().__init__()
        self.code = 40104
        self.message = CODE_MAP[self.code]
