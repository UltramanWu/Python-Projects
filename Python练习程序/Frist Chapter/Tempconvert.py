# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/6/26 14:22
"""

TempStr = input('请输入带有温度符号的温度值:')

if TempStr[-1] in ['F', 'f']:  # 如果条件成立，则执行缩进语句，否则直接跳过
    C = (eval(TempStr[0:-1])-32) / 1.8
    print('转换后的温度值是：{:.2f}C'.format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print('转换后的温度是：{:.2f}F'.format(F))
else:
    print('输入格式有误！')

