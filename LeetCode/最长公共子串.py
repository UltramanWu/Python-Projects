# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 20:54
"""
# 最长公共子串
def longestCommonPrefix(strs):
    Len = len(strs)
    if not Len:
        return ""
    for i in range(len(strs[0])):
        Global = strs[0][:i+1]
        for j in range(1, len(strs)):
            if Global != strs[j][:i+1] or i>= len(strs[j]):
                return Global[:i]
            if strs[j] == "":
                return ""
    return Global

strs = ['c', 'c']
S = longestCommonPrefix(strs)
print(S)