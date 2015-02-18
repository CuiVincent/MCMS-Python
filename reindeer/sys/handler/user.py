__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser
from reindeer.sys.model.sys_group import SysGroup
from tornado.escape import json_encode


class UserListHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_list.html')

    def post(self):
        json = SysUser.get_all_json()
        return self.write('{"success": true, "aaData":'+json+'}')


class UserAddHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_add.html')

    def post(self):
        SysUser.add("FFFF","FFFFFFF","111")
        return self.write(json_encode({'success': True}))
