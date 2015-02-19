__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base_handler
from reindeer.sys.model.sys_user import SysUser
from tornado.escape import json_encode
import random
from reindeer.sys.exceptions import BusinessRuleException


class UserListHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_list.html')

    def post(self):
        r_echo = self.get_argument('sEcho')
        r_start = int(self.get_argument('iDisplayStart'))
        r_length = int(self.get_argument('iDisplayLength'))
        r_search = self.get_argument('sSearch')
        r_sort_col = self.get_arguments('iSortCol_0')[0]
        r_sort_dir = self.get_arguments('sSortDir_0')[0]

        json = SysUser.get_slice_json(r_search, r_start, r_start+r_length, r_sort_col, r_sort_dir)
        total = SysUser.get_all_count()
        slice_total = SysUser.get_slice_count(r_search)
        r_json = '{"success": true, "aaData":'+json+',"iTotalRecords":'+str(total)+',"iTotalDisplayRecords":'+str(slice_total)+',"sEcho":'+str(r_echo)+'}'
        print(r_json)
        return self.write(r_json)


class UserAddHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_add.html')

    def post(self):
        if SysUser.add(str(random.uniform(10, 20)),"FFFFFFF","111"):
            return self.write(json_encode({'success': True}))


class UserDeleteHandler(reindeer.sys.base_handler.BaseHandler):
    def post(self):
        uids = str(self.get_argument('uid')).split(',')
        success = False
        for uid in uids:
            d_success = SysUser.delete(uid)
            if not success:
                success = d_success
        if success:
            return self.write(json_encode({'success': success}))
        else:
            raise BusinessRuleException(1152)