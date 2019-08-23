# -*- coding: utf-8 -*-
from app.views import *


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = {
            'msg': 'this is home',
            'error_msg' : None,
            'age': 20,
            'menu': ['个人中心','最新资讯','热门话题'],
            'code': '<h3>HI, 8 > 5 </h3>'
        }
        self.render('index2.html', **data)

    def post(self, *args, **kwargs):
        # 读取单个参数
        wd = self.get_argument('wd')
        # 读取多个参数名相同的参数值
        titles = self.get_arguments('title')
        # 从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        titles2 = self.get_query_arguments('title')
        print(wd2)
        print(titles2)
        print(titles)
        print(wd)

        # 从请求对象中读取参数
        req: HTTPServerRequest = self.request
        # request请求对象中的数据都是字典类型，字典中的value都是字节类型
        wd3 = req.arguments.get('wd')

        wd4 = req.query_arguments.get('wd')
        print(wd4)
        print(wd3)
        self.write('<h3>这里是主页</h3>')

    def put(self, *args, **kwargs):
        # 新增数据
        wd = self.get_argument('wd')
        wd2 = self.get_query_argument('wd')
        name = self.get_body_argument('name')
        city = self.get_argument('city')
        print(name, city, wd, wd2)
        self.write('<h3>这里是主页</h3>')

    def patch(self, *args, **kwargs):
        name = self.get_body_argument('name')
        city = self.get_argument('city')
        print(name, city)
        self.write('<h3>这里是主页</h3>')

    def delete(self, *args, **kwargs):
        city = self.get_argument('city')
        name = self.get_body_argument('name')
        print(name, city)
        self.write('<h3>这里是主页</h3>')
