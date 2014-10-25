__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
from tornado.escape import json_encode
from app_settings import app_settings
from reindeer.sys.exception import BusinessRuleException

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self._headers
        err_page = 'sys/error.html'
        err_code = status_code
        msg = '系统错误'
        info = self._reason
        back_page = app_settings["login_url"]
        if status_code == 404:
            msg = '您所访问的链接不存在'
            info = '请确认链接地址或联系管理员'
        elif status_code == 500:
            if len(kwargs['exc_info']) > 1 and kwargs['exc_info'][1]:
                exception = kwargs['exc_info'][1]
                if isinstance(exception, BusinessRuleException):
                    err_code = exception.err_code
                    msg = exception.msg
                    info = exception.info
                else:
                    info = '[' + str(err_code) + ' - ' + info + ']' + str(exception)
        else:
            if err_code:
                info = '[' + str(err_code) + ']' + info
        if self.request.headers.get("__IS_AJAX_REQUEST") == 'true':
            self.write(json_encode({'success': False, 'err_code': err_code, 'msg': msg, 'info': info}))
        else:
            self.clear()  # 防止浏览器收到错误码后重定向
            self.render(err_page, err_code=err_code, msg=msg, info=info, back_page=back_page)

    def get_current_user(self):
        user_id = self.get_secure_cookie('user_id')
        if not user_id:
            return None
        return user_id

class ErrorHandler(BaseHandler):
    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

    def check_xsrf_cookie(self):
        pass