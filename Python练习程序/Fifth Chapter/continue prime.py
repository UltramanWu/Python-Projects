# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/2 10:29
"""

# 请在...补充一行或多行代码
import math

def prime(m):
    s = ""
    count = 0
    i = int(m)
    while True:
        for j in range(2, int(math.sqrt(i))+1):
            if not i % j:
                break
        else:
            s += "{},".format(i)
            count += 1
        if count == 5:
            break
        i += 1
    return s


n = eval(input())
print(prime(n)[:-1])
