# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/2 15:22
"""


def getText():
    txt = open("hamlet.txt", 'r').read()
    txt.lower()  # 小写设置
    # 将特殊符号用空格进行替代
    for ch in "!@#$%^&*()_=-+?/,.<>{}[]|;:`~":
        txt.replace(ch, " ")
    return txt


T = getText()
words = T.split()  # 使用空格对单词进行分割
counts = {}  # 创建空词典
for ch in words:
    counts[ch] = counts.get(ch, 0) + 1

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print('{:<10}  {:>5}'.format(word, count))