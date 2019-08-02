# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 21:29
"""

def threeSum(nums):
    Len = len(nums)
    if Len < 3:
        return []
    nums.sort()  # 正向排序
    l = []  # 生成空列表
    for i in range(Len-2):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        Sum = 0 + nums[i]
        count = 0
        left = i + 1
        right = Len - 1
        while left < right:
            if count > 0:
                if nums[left-1] == nums[left]:
                    left = left + 1
                    continue
                if nums[right+1] == nums[right]:
                    right = right - 1
                    continue
            if Sum + nums[left] + nums[right] == 0:
                l.append([nums[i], nums[left], nums[right]])
                left = left + 1
                right = right - 1
                count = count + 1
            elif Sum + nums[left] + nums[right] < 0:
                left = left + 1
            else:
                right = right - 1
    return l

test = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4]
re = threeSum(test)
print(re)