# -*- coding:utf-8 -*- 
#Author: Henry

import base64

def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        for i in range(4-(len(s) % 4)):
            s = s + b'='
        return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')