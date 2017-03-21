# -*- coding:utf-8 -*- 
# Author: Henry

import threading

# 创建全局 ThreadLocal 对象
local_school = threading.local()

def student():
    # 获取local_school绑定的student
    stu = local_school.student
    print('Hello, %s in (%s)' % (stu, threading.current_thread().name))

def run_thread(name):
    # 绑定local_school的student
    local_school.student = name
    student()

t1 = threading.Thread(target=run_thread, args=('Henry',), name='Thread-A')
t2 = threading.Thread(target=run_thread, args=('Emily',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
