# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-30
Function: 栈的压入、弹出序列
"""
def isPopOrder(list1, list2):
    """
    栈的压入、弹出序列
    :param list1: 栈的压入序列
    :param list2: 栈的弹出序列
    :return: True or False
    """
    length1 = len(list1)
    length2 = len(list2)

    if length1 != length2 or length1 < 1:
        return False

    stack = []
    l1 = 0
    l2 = 0

    while l1 < length1:
        value = list1[l1]
        stack.append(value)

        while stack and stack[-1] == list2[l2]:
            # 当入栈的元素与list2的当前元素相同，则出栈，并且l2指向下一个
            stack.pop()
            l2 += 1

        if l1 == length1-1:
            # 当l1指向最后一个元素时，模拟出入栈已经结束，如果list2表示正确的出栈顺序，那么stack应该为空
            if stack:
                return False
            else:
                return True

        l1 += 1

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 3, 2, 1]
    list3 = [4, 3, 5, 1, 2]
    print isPopOrder(list1, list2)
    print isPopOrder(list1, list3)