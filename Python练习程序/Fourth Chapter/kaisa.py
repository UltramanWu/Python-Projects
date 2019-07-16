# -*- coding: UTF-8 -*-
"""

author:wu
time:2019/7/1 11:09

"""
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr(ord('a') + ((ord(c)-ord('a')) + 3)%26)
    elif 'A' <= c <= 'Z':
        t += chr(ord('A') + ((ord(c)-ord('A')) + 3)%26)
    else:
        t += c
print(t)

