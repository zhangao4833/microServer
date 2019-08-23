# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship

from utils.conn import Base




class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False, unique=True)
    url = Column(String(50), unique=True)
    note = Column(Text)
    parent_id = Column(Integer, ForeignKey('menu.id', name='parent_id_fk'))
    childs = relationship('Menu')


    def __str__(self):
        return self.title
