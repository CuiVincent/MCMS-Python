from reindeer.util.common_util import to_md5

__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from tornado.escape import json_encode

import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser
from reindeer.sys.exceptions import BusinessRuleException


class LoginHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/login.html')

    def post(self, *args, **kwargs):
        usercode = self.get_argument('usercode')
        passwd = self.get_argument('passwd')
        user = SysUser.get_by_code(usercode)
        if user:
            if to_md5(passwd) != user.PASSWORD:
                raise BusinessRuleException(1002)
            elif user.ISVALID != '0':
                raise BusinessRuleException(1003)
        else:
            raise BusinessRuleException(1001)
        self.set_secure_cookie('userid', str(user.ID), expires_days=7)
        return self.write(json_encode({'success': True}))