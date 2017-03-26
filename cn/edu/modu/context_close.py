# -*- coding:utf-8 -*- 
#Author: Henry

from contextlib import closing, contextmanager
from urllib.request import urlopen

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)