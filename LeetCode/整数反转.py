# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 11:24
"""

def reverse(self, x: int) -> int:
    if x == 0:
        return x
    Isminus = 0
    l = []
    Sum = 0
    if x < 0:
        Isminus = 1
        x = -x
    while x :
        l.append(x%10)
        x = x // 10
    for item in l:
       Sum = Sum*10 + item
    if Isminus:
        if Sum > pow(2, 31):
            Sum = 0
        else:
            Sum = -Sum
    else:
        if Sum > pow(2,31)-1:
            Sum = 0
    return Sum