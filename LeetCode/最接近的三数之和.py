# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 22:24
"""
def threeSumClosest(self, nums: list[int], target: int) -> int:
    nums.sort()
    Len = len(nums)
    Min = 65535
    MinV = 65535
    for i in range(Len - 2):
        left = i + 1
        right = Len - 1
        while left < right:
            Sum = nums[i] + nums[left] + nums[right]
            if abs(Sum - target) < Min:
                Min = abs(Sum - target)
                MinV = Sum
            elif Sum > target:
                right = right-1
            elif Sum < target:
                left = left + 1
            else:  # 如果相等直接退出
                break
        if left < right:
            break
    return MinV