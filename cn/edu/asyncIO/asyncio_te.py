# -*- coding:utf-8 -*- 
#Author: Henry

import asyncio
import threading

@asyncio.coroutine
def hello():
    print('Hello World! %s' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    n = yield from asyncio.sleep(1)
    print('Hello Again! %s' % threading.currentThread())

# 使用3.5以后新的语法，和上面的效果相同
async def hello():
    print('Hello World! %s' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    n = await asyncio.sleep(1)
    print('Hello Again! %s' % threading.currentThread())

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()