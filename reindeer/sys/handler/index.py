__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
import reindeer.sys.base_handler
from reindeer.sys.model.sys_action import SysAction
from reindeer.sys import strings


class IndexHandler(reindeer.sys.base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_name = self.get_secure_cookie('user_name')
        self.render('sys/index.html', user_name=user_name, main_menu=self.get_user_main_menu())

    def get_user_main_menu(self):
        user_id = self.get_current_user()
        parent_id = strings.action_root_main_parent
        menu = SysAction.get_action_tree_by_user_and_parent(user_id, parent_id, strings.action_type_menu_menu)
        return menu