# -*- coding:utf-8 -*- 
#Author: Henry

from collections import namedtuple, deque, defaultdict, OrderedDict
# namedtuple('属性', [属性list])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
# deque 是为了高效实现插入和删除操作的双向列表
q = deque(['a', 'b', 'c', 'd'])
q.append('e')
q.appendleft('A')
print('插入元素后的：', q)
q.popleft()
q.pop()
print('删除元素后的：', q)

dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2']) # key2 不存在返回默认值

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# OrderedDict 的key是有序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od_1 = OrderedDict()
od_1['z'] = 1
od_1['y'] = 2
od_1['x'] = 3
print(od_1)
print(list(od_1.keys())) # 按照插入的key的顺序返回