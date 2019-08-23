# -*- coding: utf-8 -*- c
from app.views import *
class OrderHandler(tornado.web.RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'python高级开发',
            'auth': 'tom',
            'price': 190
        },
        {
            'id': 2,
            'name': 'python进阶',
            'auth': 'jack',
            'price': 290
        }
    ]
    action_type = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        print('-------------initialize------------')
    def prepare(self):
        # 在初始化之后,调用行为方法之前,调用此方法进行预处理
        print('===================prepare================')
    def post(self, *args, **kwargs):
        print('++++++++++++++++++POST++++++++++++++++++++')
        self.write('post_request')
    def on_finish(self):
        print('%%%%%%%%%%%%%%%%%%on_finish%%%%%%%%%%%%%%%%%%')
    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def get(self, order_id, action_type, *args, **kwargs):
        self.write('订单查询')
        self.write(self.query(int(order_id)))
        self.write(self.action_type.get(int(action_type)))