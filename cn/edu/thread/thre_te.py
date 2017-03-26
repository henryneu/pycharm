1  # -*- coding:utf-8 -*-
2  #Author: Henry

import time, threading
# 子线程需要执行的代码
def run_thread():
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(5):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run_thread, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
