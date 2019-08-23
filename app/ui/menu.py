# -*- coding: utf-8 -*-

from tornado.web import UIModule
from utils.conn import session
from app.models.menu import Menu

class UI_Menu(UIModule):
    def render(self, *args, **kwargs):
        date = {}
        for m in session.query(Menu).filter(Menu.parent_id.is_(None)).all():
            date[m] = []
            for n in m.childs:
                date[m].append(n)
        data = {
            'menu': date
        }
        return self.render_string('ui/menu.html', **data)
