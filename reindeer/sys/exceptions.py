__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

err_codes = {
    1001: ['登录失败', '您所输入的账号不存在' ],
    1002: ['登录失败', '密码错误' ],
    1003: ['登录失败', '该账号已被停止使用'],
    1101: ['注册失败', '该用户名已存在']
}


class BusinessRuleException(Exception):
    def __init__(self, err_code):
        self.err_code = err_code
        try:
            self.msg = err_codes[self.err_code][0]
        except KeyError:
            self.msg = '未知错误'
        try:
            self.info = err_codes[self.err_code][1]
        except KeyError:
            self.info = '请稍后再试'

    def __str__(self):
        message = "BusinessRule [%d - %s] %s" % (self.err_code, self.msg, self.info)
        return message