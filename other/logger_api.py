# -*- coding: utf-8 -*-
import tornado.web as web
import tornado.ioloop as ioloop


class LoggerHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        print(self.get_argument('name'), self.get_argument('asctime'), self.get_argument('levelname'),
              self.get_argument('msg'))


if __name__ == '__main__':
    app = web.Application([
        ('/', LoggerHandler)
    ])
    app.listen(port=8000)
    ioloop.IOLoop.current().start()
