# -*- coding: utf-8 -*-
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop



class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 向客户端相应数据
        self.write('<h3>hello word!</h3>')

if __name__ == '__main__':
    # 创建WEB应用
    app = Application(handlers=[
        ('/', IndexHandler)
    ])
    # 绑定端口
    app.listen(port=7000)
    # 启动WEB服务
    print('starting http://localhost:7000')
    IOLoop.current().start()