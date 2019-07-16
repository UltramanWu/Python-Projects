# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 21:34
"""
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs('string'))