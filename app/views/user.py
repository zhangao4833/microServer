# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class UserHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('''
        <form method='post'>
        <input name='name'>
        <input type='submit' value='登陆'>
        </from>
        ''')
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')

        # 以安全的方式写入到cookie中

        self.set_secure_cookie('username', name)

        self.redirect('/robbit')