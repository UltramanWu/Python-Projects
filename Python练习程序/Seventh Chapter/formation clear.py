# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/3 10:44
"""
f = open('data.csv')
fls = list(f)
fls = fls[::-1]  # 行已经倒序排列
for ls in fls:
    ls = ls.replace('\n', '')
    ls = ls.replace(' ', '')
    data = ls.split(',')
    data = data[::-1]
    print(';'.join(data))
f.close()
