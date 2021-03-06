# -*- coding: utf-8 -*-


"""
    自定义错误码，与自定义exception配合使用
"""
from template_babel import get_lazy_text as _

# 注意: 这个CODE_MAP具体会返回一个LazyString对象,如果需要进行字符串拼接,需要先str()进行转换
CODE_MAP = {
    # 200
    20000: _('成功'),
    # 400
    40000: _('客户端发送了不合法的请求'),  # Bad Request
    40001: _('参数 [%s] 类型错误，应为 [%s]'),
    40002: _('不合法的参数: %s'),
    40003: _('关键参数缺失: [%s]'),
    # 401
    40100: _('身份验证失败'),
    # 404
    40400: _('资源未找到'),
    # 500
    50000: _('服务器未知异常'),
}
