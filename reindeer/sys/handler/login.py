__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from tornado.escape import json_encode
import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser
from reindeer.sys.model.sys_group import SysGroup
from reindeer.sys.exceptions import BusinessRuleException
from reindeer.util.common_util import to_md5


class LoginHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/login.html')

    def post(self, *args, **kwargs):
        user_code = self.get_argument('user_code')
        pass_wd = self.get_argument('pass_wd')

        user = SysUser.get_by_code(user_code)
        if user:
            if to_md5(pass_wd) != user.PASSWORD:
                raise BusinessRuleException(1002)
            elif user.STATUS != 1:
                raise BusinessRuleException(1003)
        else:
            raise BusinessRuleException(1001)
        self.set_secure_cookie('user_id', str(user.ID), expires_days=7)
        self.set_secure_cookie('user_name', str(user.NAME), expires_days=7)
        return self.write(json_encode({'success': True}))