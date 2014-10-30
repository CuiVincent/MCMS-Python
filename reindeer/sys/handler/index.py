__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
import reindeer.sys.base_handler
from reindeer.sys.model.sys_action import SysAction
from reindeer.util import common_util

class IndexHandler(reindeer.sys.base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_name = self.get_secure_cookie('user_name')
        self.render('sys/index.html', user_name=user_name, user_menu_html=self.user_menu_html())

    def user_menu_html(self):
        user_id = self.get_current_user()
        parent_id = common_util.action_root_main_parent
        return  str(SysAction.get_tree_by_user_and_parent(user_id,parent_id))