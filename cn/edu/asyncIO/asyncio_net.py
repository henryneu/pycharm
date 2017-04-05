# -*- coding:utf-8 -*- 
#Author: Henry

import asyncio

@asyncio.coroutine
def apply(host):
    print('get info from %s' % host)
    con = asyncio.open_connection(host, 80)
    reader, writer = yield from con
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()

# 使用3.5以后新的语法，和上面的效果相同
async def apply(host):
    print('get info from %s' % host)
    con = asyncio.open_connection(host, 80)
    reader, writer = await con
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [apply(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()