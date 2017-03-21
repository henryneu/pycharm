from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('today is ')
    f.write(datetime.now().strftime('%Y-%M-%D'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

with open('case.txt', 'r') as f1:
    s = f1.readline()  #  每次读取一行文件
    print('open as readline...')
    print(s)

with open('case.txt', 'r') as f1:
    print('open as readlines...')
    for line in f1.readlines():  #  一次读取所有内容并按行返回list
        print(line.strip())