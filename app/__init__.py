# -*- coding: utf-8 -*-
import os

import tornado.web

from app.ui.menu import UI_Menu
from app.views.cookie_v import CookieHandler
from app.views.download import DownloadHandler, AsyncDownloadHandler, Async2DownloadHandler
from app.views.index_v import IndexHandler
from app.views.menu.m_index import MenuIndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')
settings = {
    'debug': True,
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH,
    'static_url_prefix': '/s/',
    'ui_modules': {
        'UI_Menu' : UI_Menu
}
}


def make_app(host):
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<order_id>\d+)/(?P<action_type>\d+)/', OrderHandler),
        ('/menu', MenuIndexHandler),
        ('/download', DownloadHandler),
        ('/async_download', AsyncDownloadHandler),
        ('/async2_download', Async2DownloadHandler)
    ], default_host=host, **settings)
