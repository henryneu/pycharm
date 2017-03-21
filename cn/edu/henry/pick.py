import pickle
import json

d = dict(name='Henry', age=24, score=98)
print('d', d)
# 序列化
date = pickle.dumps(d)
print('dict to pickle', date)
stu = json.dumps(d)
print('dict to json', stu)
# 反序列化
print('pickle to dict', pickle.loads(date))
print('json to dict', json.loads(stu))

# 序列化为 file-like Object
f = open('pick.txt', 'wb')
pickle.dump(d, f)
f.close()
# 反序列化
f = open('pick.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)