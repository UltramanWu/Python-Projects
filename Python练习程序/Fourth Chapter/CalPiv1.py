# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 15:58
"""
# CalPiv1.py

from random import random
from time import perf_counter

num = 1000*1000
fit = 0
start = perf_counter()
for i in range(1, num+1):
    x, y = random(), random()
    if pow(x**2 + y**2, 0.5) <= 1:
        fit += 1
pi = 4 * (fit/num)
print('PI的值为{0}'.format(pi))
print('程序运行时间为{:.3f}s'.format(perf_counter()-start))

