# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 17:09
"""
# four flower number
for i in range(1000,10000):
    a = i//1000
    b = (i%1000)//100
    c = (i%100)//10
    d = i%10
    num = pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)
    if num == i:
        print(i)