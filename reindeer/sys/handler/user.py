__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser


class UserHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        users = SysUser.get_all()
        self.render('sys/user_list.html', users=users)

