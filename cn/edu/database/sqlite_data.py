# -*- coding:utf-8 -*- 
#Author: Henry

import sqlite3

# 初始化数据库
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
except:
    print('Error')
finally:
    cursor.close()
    conn.commit()
    conn.close()

def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('select name from user where score between ? and ? order by score', (low, high))
        values = cursor.fetchall()
        return list(map(lambda x:x[0], values))
    except:
        print('Error')
    finally:
        cursor.close()
        conn.commit()
        conn.close()

if __name__ == '__main__':
    print(get_score_in(80, 95))
    print(get_score_in(60, 80))
    print(get_score_in(60, 100))