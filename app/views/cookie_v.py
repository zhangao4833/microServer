# -*- coding: utf-8 -*-
from app.views import *

class CookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 从查询参数中读取Cookie的名称
        # 验证参数中是否存在name
        li = []
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            value = self.get_cookie(name)
            self.write(value)
        else:
            for k, v in self.cookies.items():
                print(k)
                li.extend([k, self.get_cookie(k)])
        html = str(li) + '''
        <form method='post'>
        <input type='text' name='name' />
        <input type='submit' value='提交'>
        </form>
        '''
        self.write(html)

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        if self.cookies.get(name, None):
            self.clear_cookie(name)
            self.write('删除成功')
        else:
            self.write('cookie  %s  不存在' % name)
        # 重定向操作时，不需要操作self.write()
        self.redirect('/cookie')
