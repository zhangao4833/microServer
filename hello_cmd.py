# -*- coding: utf-8 -*-
import datetime
import json
import os
import time

import tornado.web as web
import tornado.ioloop as ioloop
from tornado.options import define, options

# 定义命令行参数
define('port', default=8000, type=int, help='set you server port')


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 获取请求的查询参数
        wd = self.get_argument('wd')

        self.write('Hello Tronado!<p>wd: %s </p>' % wd)

    def post(self, *args, **kwargs):
        wd = self.get_argument('wd')
        self.write('Post request! Hello post wd : %s' % wd)


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('jack', 'tornado', expires=datetime.datetime.now() + datetime.timedelta(3))
        self.set_header('Content-Type', 'text/html')
        self.write('hello login!')


class LogoutHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello logout!')


class ReHandler(web.RequestHandler):
    def get(self, name, *args, **kwargs):
        self.write('this re%s' % name)


class DeleteHandler(web.RequestHandler):
    def initialize(self):
        print('初始化资源')
        time.sleep(2)

    def prepare(self):
        print()
        print('预处理')
        time.sleep(2)

    def on_finish(self):
        print('释放资源')
        time.sleep(2)

    def delete(self, *args, **kwargs):
        self.write('oh delete！')


class JsonHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        if 'json' in str(self.request.headers.get('Content-Type')):
            # 判断请求头里面的数据类型是不是json
            print(json.loads(self.request.body.decode('utf-8')))
            # 反序列化
            self.set_header('Content-Type', 'Application/json')
            self.write(self.request.body)
        else:
            self.write('你的数据不是json格式')


class TempalteHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        data = {'name': 'Tom', 'sex': 'F'}
        self.render('index.html', **data)


if __name__ == '__main__':
    # 解析命令行中的参数,类似于sys.argv的数据解析
    options.parse_command_line()
    # 声明web服务请求资源
    app = web.Application([
        ('/', IndexHandler),
        ('/login', LoginHandler),
        ('/logout', LogoutHandler),
        (r'/(?P<name>\d{5,})', ReHandler),
        ('/delete', DeleteHandler),
        ('/jsondata', JsonHandler),
        ('/template', TempalteHandler)
    ], template_path=os.path.join(os.path.dirname(__file__), 'templates'))
    app.listen(options.port)
    ioloop.IOLoop.current().start()
