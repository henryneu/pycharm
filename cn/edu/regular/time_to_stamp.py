# -*- coding:utf-8 -*- 
#Author: Henry

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str,tz_str):
    dt_date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_utc = dt_date.replace(tzinfo=timezone.utc)  # 强制设置为UTC + 0:00
    tz_group = re.match(r'^UTC([\+\-])(\d+):(\d+)$',tz_str)
    if '+' == tz_group.group(1):
        dt =dt_utc.replace(tzinfo=timezone(timedelta(hours=int(tz_group.group(2)), minutes=int(tz_group.group(3)))))
    else:
        dt = dt_utc.replace(tzinfo=timezone(timedelta(hours= - int(tz_group.group(2)), minutes=int(tz_group.group(3)))))
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')