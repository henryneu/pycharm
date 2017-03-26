# -*- coding:utf-8 -*- 
# Author: Henry

import hashlib
# 存储用户名和密码的数据库
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def register(user, password):
    db[user] = calc_md5(password + user + 'the-Salt')

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(user, password):
    # 判断所输入的password是否和数据库中的匹配
    # res_md5 = calc_md5(password)
    res_md5 = calc_md5(password + user + "the-Salt")
    if res_md5 == db[user]:
        print('密码输入正确，可以正常访问！')
    else:
        print('密码输入错误，拒绝访问！')

if __name__ == '__main__':
    login('bob','abc999')
    login('michael', '123456')
    login('alice','alice2008')
    # 注册时使用加盐的password
    register('henry','5201314')
    login('henry','5201314')