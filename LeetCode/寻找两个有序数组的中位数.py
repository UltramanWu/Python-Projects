# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/30 9:01
"""


def findMedianSortedArrays(nums1, nums2) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return self.findMedianSortedArrays(nums2, nums1)  # 保证左侧的列表中元素小于右侧列表元素个数
    k = (n1 + n2 + 1) // 2  # 保证左侧的元素个数为整体个数的一半
    left = 0
    right = n1
    while left < right:
        m1 = (left + right) // 2  # 使用二分法
        m2 = k - m1
        if nums1[m1] < nums2[m2 - 1]:  # 如果此时数组右侧最小值小于右侧左侧最大值
            left = m1 + 1
        else:
            right = m1
    m1 = left
    m2 = k - m1
    # 获取合并数组中左侧的最大值
    c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
    if (n1 + n2) % 2 == 1:
        return c1
    # 获取合并数组中右侧的最小值
    c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
    return (c1 + c2) / 2


nums1 = [1, 2, 5, 7]
nums2 = [3, 4, 8, 9]
Result = findMedianSortedArrays(nums1, nums2)
print(Result)
