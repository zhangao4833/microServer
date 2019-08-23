# -*- coding: utf-8 -*-
import json
import uuid

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
from tornado.options import define, options, parse_command_line


class LoginHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, accept, content-type")
        self.set_header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS")
        self.set_header('Content-Type', 'application/json')

    user = [
        {
            'id': 1,
            'name': 'jack',
            'pwd': '123',
            'phone': '1231231231',
            'city': '上海',
            'last_login_device': 'Android 5.1 OnePlus5'
        }
    ]

    def get(self, *args, **kwargs):
        bytes = self.request.body
        content_type = self.request.headers.get('Content-Type')
        resp_data = {}
        print(content_type)
        if content_type.startswith('application/json'):
            # self.write('OK')
            json_str = bytes.decode('utf-8')
            data_dict = json.loads(json_str)
            print(data_dict['name'], data_dict['pwd'])
            login_user = None
            for user in self.user:
                if user['name'] == data_dict['name']:
                    if user['pwd'] == data_dict['pwd']:
                        login_user = user['name']
                        break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此用户或用户密码错误'

            self.write(resp_data)
            self.set_header('Content-Type', 'application/json')

        else:
            self.write('upload data should json')

    def post(self, *args, **kwargs):
        bytes = self.request.body
        content_type = self.request.headers.get('Content-Type')
        print(content_type)
        resp_data = {}
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            data_dict = json.loads(json_str)
            if all((data_dict.get('name'), data_dict.get('pwd'), data_dict.get('phone'), data_dict.get('city'))):
                data_dict['id'] = int(self.user[-1]['id']) + 1
                self.user.append(data_dict)
                resp_data['msg'] = 'success'
                resp_data['user_id'] = data_dict['id']
                data_dict.setdefault('last_login_device', 'PC')
            else:
                resp_data['msg'] = '用户名和密码以及手机号和城市必须不为空'
        else:
            resp_data['msg'] = '数据不为json，添加失败'
        print(self.user)
        self.write(resp_data)

    def put(self, *args, **kwargs):
        bytes = self.request.body
        content_type = self.request.headers.get('Content-Type')
        print(content_type)
        resp_data = {}
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            data_dict = json.loads(json_str)
            for u in self.user:
                if u['id'] == int(data_dict['user_id']):
                    for k, v in data_dict.items():
                        if k in u:
                            u[k] = v
                    resp_data['msg'] = 'success'
                    break
        else:
            resp_data['msg'] = '数据不为json，添加失败'
        print(self.user)
        self.write(resp_data)

    def delete(self, *args, **kwargs):
        bytes = self.request.body
        content_type = self.request.headers.get('Content-Type')
        print(content_type)
        resp_data = {}
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            data_dict = json.loads(json_str)
            for u in self.user:
                if u['id'] == int(data_dict['user_id']):
                    self.user.remove(u)
                    resp_data['msg'] = 'success'
        else:
            resp_data['msg'] = '数据不为json，添加失败'
        print(self.user)
        self.write(resp_data)
    def options(self, *args, **kwargs):
        self.set_status(200)


def make_app():
    return Application([
        ('/user', LoginHandler)
    ], default_host=options.h)


if __name__ == '__main__':
    define(name='h', type=str, help='set host', default='127.0.0.1')
    define(name='p', type=int, help='set port', default=8000)
    parse_command_line()

    app = make_app()
    app.listen(options.p)
    IOLoop.current().start()
