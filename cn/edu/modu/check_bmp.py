# -*- coding:utf-8 -*- 
#Author: Henry

import struct

byte_1 = struct.pack('>I', 10240099) # >I：> 表示字节顺序是网络序；I 表示4字节无符号整数
print(byte_1)
int_1 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(int_1)
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
byte_2 = struct.unpack('<ccIIIIIIHH', s)
print(byte_2)

def checkBMP(name):
    with open(name, 'rb') as f:
        s = f.read(30)
    struct_file = struct.unpack('<ccIIIIIIHH', s)
    if s[0]==b'B' and s[1]==b'M':
        print('%s is a bmp file' %name)
        print('width is %s height is %s' % (s[6], s[7]))
        print('size is %s' %s[2])
        print('color is %s' %s[9])
    else:
        print('%s is not a bmp file' %name)

file_name = input('please input file name:')
checkBMP(file_name)