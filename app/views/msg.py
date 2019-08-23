# -*- coding: utf-8 -*-
import random
import time

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class RobbitHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('msg/robbit.html')


class MsgHandler_old(WebSocketHandler):
    # 当前处理器是长连接
    def open(self, *args, **kwargs):
        # 客户端请求连接
        ip = self.request.remote_ip
        # 向客户端发送消息
        self.write_message('是谁？ -- %s' % ip)

        # 每间隔1s发送一个幸运数字
        self.write_message('starting')
        for i in range(10):
            time.sleep(1)
            self.write_message('你的幸运数字为 %s' % random.randint(100, 1000))
        self.write_message('end')


class MsgHandler(WebSocketHandler):
    # 当前处理器是长连接
    online_client = []
    def send_all(self, msg):
        for client in self.online_client:
            client.write_message(msg)
    def open(self, *args, **kwargs):
        # 客户端请求连接
        ip = self.request.remote_ip

        username = self.get_secure_cookie('username')

        # 向客户端发送消息

        self.online_client.append(self)
        msg = '%s 链接到服务器 -- %s' % (username.decode('utf-8'), ip)
        self.send_all(msg)
        # self.write_message()

    def on_message(self, message):
        msg = '%s 说：%s' % (self.get_secure_cookie('username').decode('utf-8'), message)
        self.send_all(msg)

    def on_connection_close(self):
        self.send_all('%s 退出了服务器' % self.request.remote_ip)
        self.online_client.remove(self)