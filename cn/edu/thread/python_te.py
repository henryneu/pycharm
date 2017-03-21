# -*- coding:utf-8 -*-
#Author: Henry
# 线程不加锁的情况 balance 会出现错误
import time, threading

balance = 0
lock = threading.Lock()

def change_bal(n):
    global balance
    # 先加后减
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        try:
            change_bal(n)
        finally:
            # 释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('The balance: ', balance)