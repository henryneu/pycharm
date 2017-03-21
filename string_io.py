from io import StringIO
from io import BytesIO
# 内存中读写字符
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# 内存中读写二进制数
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())