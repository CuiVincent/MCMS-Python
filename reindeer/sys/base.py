__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
from tornado.escape import json_encode
from app_settings import app_settings

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self._headers
        err_page = 'sys/error.html'
        err_code = status_code
        msg = '系统错误'
        info = self._reason
        if len(kwargs['exc_info']) > 1 and len(kwargs['exc_info'][1].args) > 0:
            info = kwargs['exc_info'][1].args[0]
        back_page = app_settings["login_url"]
        if status_code == 404:
            msg = '您所访问的链接不存在'
            info = '请确认链接地址或联系管理员'
        elif status_code == 500:
            pass
        else:
            if err_code:
                info = '[' + str(err_code) + ']' + info
        if self.request.headers.get("__IS_AJAX_REQUEST") == 'true':
            self.write(json_encode({'success': False, 'err_code': err_code, 'msg': msg, 'info': info}))
        else:
            self.clear()  # 防止浏览器收到错误码后重定向
            self.render(err_page, err_code=err_code, msg=msg, info=info, back_page=back_page)

class ErrorHandler(BaseHandler):
    """Generates an error response with ``status_code`` for all requests."""
    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

    def check_xsrf_cookie(self):
        # POSTs to an ErrorHandler don't actually have side effects,
        # so we don't need to check the xsrf token.  This allows POSTs
        # to the wrong url to return a 404 instead of 403.
        pass