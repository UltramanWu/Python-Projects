# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 15:23
"""
def intToRoman(num):
    if not num:  # 如果当前数字为0
        return ""
    NumStr = ""
    l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    lStr = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    for i in range(13):
        if num // l[i]:
            NumStr = NumStr + lStr[i] * (num // l[i])
            num = num % l[i]
    return NumStr


a = eval(input())
b = intToRoman(a)
print(b)