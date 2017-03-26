# -*- coding:utf-8 -*- 
#Author: Henry

import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print(n)

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
# 重复输出10个A
np = itertools.repeat("A", 10)
for p in np:
    print(p)
# 把一组迭代对象串联起来
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
# 迭代器中相同元素分组放在一起
for key, group in itertools.groupby('AaaBBbccCAAaA', lambda c:c.upper()):
    print(key, list(group))