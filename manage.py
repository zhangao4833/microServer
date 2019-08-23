# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.options
from tornado.options import define
from app import make_app





if __name__ == '__main__':
    define('port', default=8000, type=int, help='set tornado start port')
    define('host', default='127.0.0.1', type=str, help='set tornado start host')
    tornado.options.parse_command_line()
    app = make_app(tornado.options.options.host)
    app.listen(tornado.options.options.port)
    # 启动服务
    print('Tornado Serve Start to http://%s:%s' % (tornado.options.options.host, tornado.options.options.port))
    tornado.ioloop.IOLoop.current().start()
