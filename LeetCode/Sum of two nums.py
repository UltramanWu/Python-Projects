# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/29 20:08
"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    Len = len(nums)
    if Len < 2:
        return []
    dict1 = {}  ## 空字典
    Save: List[int] = []  ## 列表
    dict1[nums[0]] = 0
    for i in range(1, len(nums)):
        if target-nums[i] in dict1:
            Save.append(dict1.get(target-nums[i]))
            Save.append(i)
            break
        dict1[nums[i]] = i  ## 将数据导入到字典中
    return Save


