# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/6 17:08
"""
#import sys
#print('RECLIMIT:{}'.format(sys.getrecursionlimit()))
#print('EXEPATH:{}'.format(sys.executable))
#print('UNICODE:{}'.format(sys.maxunicode))
#print('RECLIMIT:{},EXEPATH:{},UNICODE:{}'.\
#      format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))
f = open('latex.log')
s = list(f)
for c in s:
    c.replace('\n', '')
    c.replace(' ', '')
ls = list(set(s))
for ch in ls:
    s.remove(ch)

lt = list(set(s))

print('共{}关键行'.format(len(ls)-len(lt)))