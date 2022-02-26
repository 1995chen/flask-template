# -*- coding: utf-8 -*-


# 自定义错误码，与exception.py配合使用
from template_babel import get_lazy_text as _

# 注意: 这个CODE_MAP具体会返回一个LazyString对象,如果需要进行字符串拼接,需要先str()进行转换
CODE_MAP = {
    20000: _('成功'),
    4001: _('客户端发送了不合法的请求'),  # Bad Request
    40001: _('参数 [%s] 类型错误，应为 [%s]'),
    40002: _('不合法的枚举参数 [%s], 可选值： [%s]'),
    40003: _('不合法的JSON字符串'),
    40004: _('不合法的参数: %s'),
    40005: _('记录已存在'),
    40007: _('[%s] 已存在'),
    40008: _('[%s] 不符合正则规则：[%s]'),
    40009: _('此申请已经被处理，请刷新查看最新状态'),
    40010: _('关键参数缺失: [%s]'),
    40012: _('数据库连接失败!\n错误信息:\n%s'),
    40013: _('记录未找到，可能已被删除'),
    40100: _('请先登录'),  # Unauthorized
    40101: _('用户未找到'),
    40103: _('抱歉，您没有此操作的权限'),
    40104: _('身份验证失败'),
    40404: _('打点模块发送失败'),

    5001: _('服务器未知异常'),

}
