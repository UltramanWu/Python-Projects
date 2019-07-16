# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/2 11:49
"""


# CalStastiscV1


def GetNum():
    num = []
    item = input('请输入一个数据：')
    while item != "":
        num.append(eval(item))
        item = input('请输入一个数据：')
    else:
        return num


def mean(num):
    Sum = 0.0
    for digit in num:
        Sum += digit
    return Sum / len(num)


def median(num):
    sorted(num)
    if len(num) % 2:
        return num[len(num) // 2]
    else:
        return (num[len(num) // 2 - 1] + num[len(num) // 2]) / 2


def dev(num, middle):
    Sum = 0.0
    for data in num:
        Sum += (data - middle) ** 2
    return Sum


n = GetNum()
m = mean(n)
print("平均值：{},方差：{:.3f},中位数：{}".format(m, dev(n, m), median(n)))
