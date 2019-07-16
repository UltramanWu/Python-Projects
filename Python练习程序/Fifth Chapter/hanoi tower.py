# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 21:36
"""


def hanoi(n: object, src: object, dst: object, mid: object) -> object:
    if n == 1:
        print('{}->{}'.format(src, dst))
    else:
        hanoi(n - 1, src, mid, dst)
        print(f'{src}->{dst}')
        hanoi(n - 1, mid, dst, mid)


hanoi(3, 'x', 'y', 'z')
