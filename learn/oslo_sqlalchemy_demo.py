"""
如下两张表，映射后的类如下：
create table users (
    id integer not null,
    name vchar,
    fullname vchar,
    passwd vchar,
    primary key (id)
);
create table address (
    id integer not null,
    user_id integer,
    primary key (id),
    foreign key (user_id) reference users (id)
);
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# 1. define base
Base = declarative_base()

# 2. define ORM class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True);
    name = Column(String);
    fullname = Column(String);
    passwd = Column(String);

class Address(object):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True);
    user_id = Column(Integer, ForeignKey('users.id'));


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_session(CONF) # CONF中有DB的URL，根据这个创建session
Session = sessionmaker(bind=engine) # 配置Session
session = Session() # 工厂模式初始化session，在neutron中session都是get到的

for u, a in session.query(User, Address).\
            filter(User.id == Address.user_id).\
            all():
    print u, a
# 这个就等价于：
'''
select users.id, users.name, users.passwd, address.id
from users, address
where users.id == address.user_id
'''
