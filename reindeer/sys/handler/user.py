__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser


class UserListHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_list.html')

    def post(self):
        json = SysUser.get_all_json()
        return self.write('{"success": true, "aaData":'+json+'}')
