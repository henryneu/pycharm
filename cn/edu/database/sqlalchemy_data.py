# -*- coding:utf-8 -*-
# Author: Henry

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector

# 创建表
conn = mysql.connector.connect(user='root', password='5201314', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')
cursor.execute('create table if not exists book (id varchar(20) primary key, name varchar(20), user_id integer)')
cursor.close()
# 创建对象的基类
Base = declarative_base()

# 定义user对象
class User(Base):
    # 表名
    __tablename__ = 'user'
    # 对象所对应的表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接
init_d = create_engine('mysql+mysqlconnector://root:5201314@localhost:3306/test')
# 创建DBsession类型
DBsession = sessionmaker(bind=init_d)
# 创建session对象
session = DBsession()
# 创建要加入的新user对象
# new_user = User(id='4', name='Lucy')
# 添加到session
# session.add(new_user)
# 提交即保存到数据库
session.commit()
# # 创建新的book对象
# new_book1 = Book(id='0107', name='python', user_id='4')
# session.add(new_book1)
# session.commit()
# new_book2 = Book(id='0108', name='database', user_id='4')
# session.add(new_book2)
# session.commit()
# 关闭session
session.close()

session = DBsession()
# user = session.query(User).filter(User.id=='6').one()
user = session.query(User).filter(User.id == '1').all()
# print('type:', type(user))
# print('name:', user.name)
print(user)
for b in user:
    print(b.books)
session.close()
