# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/29 20:40
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1==None and l2==None:
        return None
    elif l1==None:
        return l2
    elif l2==None:
        return l1

    carry = 0
    Savelist = ListNode(0)
    head = Savelist
    while l1 and l2:
        BitSum = l1.val + l2.val + carry
        Add = ListNode(BitSum % 10)
        carry = BitSum // 10
        head.next = Add
        head = Add  #向后移动
        l1 = l1.next
        l2 = l2.next

    while l1:
        BitSum = l1.val + carry
        Add = ListNode(BitSum % 10)
        carry = BitSum // 10
        head.next = Add
        head = Add  #向后移动
        l1 = l1.next
    while l2:
        BitSum = l2.val + carry
        Add = ListNode(BitSum % 10)
        carry = BitSum // 10
        head.next = Add
        head = Add
        l2 = l2.next
    if carry:
        Add = ListNode(1)
        head.next = Add

    return Savelist.next