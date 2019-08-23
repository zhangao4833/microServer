# -*- coding: utf-8 -*-

from unittest import TestCase

from utils.conn import session

from app.models.menu import Menu


class TestMenu(TestCase):
    def test_add(self):
        # m1 = Menu(title='用户管理')
        # session.add(m1)
        session.add_all([Menu(title='订单管理'), Menu(title='会员管理', url='/user1', parent_id=1),
                         Menu(title='派件员', url='/user2', parent_id=1), Menu(title='合作商', url='/user3', parent_id=1),
                         Menu(title='订单统计', url='/order_cnt', parent_id=2)])
        session.commit()
    def test_get(self):
        # 查询-session.query(模型类)
        m = session.query(Menu).get(1)
        print(m.title)
        print('------子菜单-------')
        for cm in m.childs:
            print(cm.title)
    def test_query_root_menu(self):
        # 查看所有的一级菜单
        ms = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for m in ms:
            print(m.title)
            for mc in m.childs:
                print('|---',mc.title)
    def test_update(self):
        mn = session.query(Menu).get(5)
        # mn.title = '合作伙伴'
        mn.parent_id = 1
        session.commit()

    def test_move(self):
        mn = session.query(Menu).get(5)
        session.delete(mn)
        session.commit()