# -*- coding:utf-8 -*- 
#Author: Henry

from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    # def __enter__(self):
    #     print('Begin')
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if exc_type:
    #         print('Error')
    #     else:
    #         print('End')

    def query(self):
        print('Query info about %s...' % self.name)

# with Query('Henry') as q:
#     q.query()
# contextmanager 通过编写generator来简化上下文管理
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Henry') as q:
    q.query()