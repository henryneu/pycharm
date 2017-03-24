# -*- coding:utf-8 -*- 
#Author: Henry

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

lo = LastUpdatedOrderedDict(5)
lo.__setitem__('a', 1)
lo.__setitem__('b', 2)
lo.__setitem__('c', 3)
lo.__setitem__('d', 4)
lo.__setitem__('e', 5)
lo.__setitem__('f', 6)
print(lo)