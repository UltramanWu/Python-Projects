# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/6 9:58
"""

from random import random


# 打印提示信息
def printInfo():
    print('请输入双方选手的势力值以及比赛场次ProA,ProB,N')
    print('势力值在0~1之间:', end="")


# 获得输出结果
def getInput():
    return eval(input())


# 判断一场比赛是否结束
def GameOver(winsA, winsB):
    return winsA == 15 or winsB == 15


# 模拟一场比赛
def simOnegame(proA, proB):
    ScoreA = ScoreB = 0
    Priority = 'A'
    while not GameOver(ScoreA, ScoreB):
        if Priority == 'A':
            if random() < proA:
                ScoreA += 1
            else:
                Priority = 'B'
        else:
            if random() < proB:
                ScoreB += 1
            else:
                Priority = 'A'
    return ScoreA, ScoreB


# 模拟n场比赛
def simNgame(n, proA, proB):
    countN = 0
    winsA = winsB = 0
    while countN < n:
        ScoreA, ScoreB = simOnegame(proA, proB)
        if ScoreA > ScoreB:
            winsA += 1
        else:
            winsB += 1
        countN += 1
    return winsA, winsB


# 打印比赛结果
def printSummary(winsA, winsB):
    n = winsA + winsB
    print('一共进行了{}场比赛'.format(n))
    print('A胜出场数为{},占总场数的{:0.1%}'.format(winsA, winsA / n))
    print('B胜出场数为{},占总场数的{:0.1%}'.format(winsB, winsB / n))


def main():
    printInfo()
    ProA, ProB, n = getInput()
    winsA, winsB = simNgame(n, ProA, ProB)
    printSummary(winsA, winsB)

main()