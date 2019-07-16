# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 16:44
"""
s = ""
for i in range(100, 1000):
    a = i//100
    b = (i % 100)//10
    c = i % 10
    if i == pow(a, 3)+pow(b, 3)+pow(c, 3):
      s += '{},'.format(i)
print(s[:-1])
