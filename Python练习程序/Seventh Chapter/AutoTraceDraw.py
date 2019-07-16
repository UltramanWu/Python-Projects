# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/2 20:15
"""

import turtle as t

t.title('自动绘制轨迹')
t.setup(800, 600)
t.pensize(5)
t.pencolor('red')
# 数据读取
f = open('data.txt')
datals = []
for line in f:
    line = line.replace('\n', ' ')
    datals.append(list(map(eval, line.split(','))))
f.close()

# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()
