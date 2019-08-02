# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 10:39
"""

def convert(self, s: str, numRows: int) -> str:
    if s == "":
        return s

    l = []
    for i in range(numRows):
        l.append('')
    ptr = 1
    count = 0
    for ch in s:
        l[count] = l[count] + ch
        count = count +ptr
        if count % 3 == 0:
            ptr = -ptr
    for Str in l:
        SumStr = SumStr + Str
    return SumStr


def convert(self, s: str, numRows: int) -> str:
    if s == "" or numRows == 1:
        return s
    # 创建链表
    dict1 = {}
    SumStr = ''
    for i in range(numRows):
        dict1[i] = ""
    ptr = 1
    count = 0
    for ch in s:
        dict[count] = dict[count] + ch
        count = count + ptr
        if count % (numRows-1) == 0:
            ptr = -ptr
    for di in dict1:
        SumStr = SumStr + dict[di]
    return SumStr