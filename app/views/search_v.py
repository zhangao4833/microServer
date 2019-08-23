# -*- coding: utf-8 -*-
from app.views import *

class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        'python': 'python世界第一',
        'java': '用量最大',
        'H5': 'H5全称HTML5，于2014流行的前端web标签语言'
    }

    def get(self, *args, **kwargs):
        html = '''
        <h3>搜索 %s 结果</h3>
        <p> %s </p>
        '''
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)
        # self.write(html % (wd, result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))
        self.set_header('Content-Type', 'application/json')
        self.set_cookie('wd', wd)
        self.set_status(200)
