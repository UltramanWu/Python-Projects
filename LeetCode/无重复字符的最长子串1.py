# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/29 21:26
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    Len = len(str)
    if Len <= 1:
        return Len
    Start = 0
    Max_Len = 0
    for i in range(1, Len):
        if s[i] in s[:i]:
            Strlen = i - start
            if Strlen > Max_Len:
                Max_Len = Strlen
            start = s[:i].find(s[i], start, i - 1) + 1
    if Strlen > Max_Len:
        Max_Len = Strlen

    return Max_Len


