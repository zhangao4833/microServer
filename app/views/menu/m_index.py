# -*- coding: utf-8 -*-
from tornado.web import RequestHandler

from app.models.menu import Menu
from utils.conn import session


class MenuIndexHandler(RequestHandler):
    def render(self, template_name, **kwargs):
        data = {
            'menu': session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        }
        return self.render_string('menu/index.html', **data)
