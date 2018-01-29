# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 调整数组顺序使奇数位于偶数前面
"""
def ReOrderArray1(lists):
    """
    新创建一个数组
        时空复杂度均为O(n)
    :param lists:
    :return:
    """
    if len(lists) == 0:
        return []
    newlist = []

    for i in range(0, len(lists)):
        if lists[i] % 2 == 1:
            newlist.append(lists[i])

    for i in range(0, len(lists)):
        if lists[i] % 2 == 0:
            newlist.append(lists[i])

    return newlist

def ReOrderArray2(lists):
    """
    左右两个指针
        注：奇数、偶数可扩展成辅助判断函数的问题（可扩展性）
    :param lists:
    :return:
    """
    if len(lists) == 0:
        return []

    left = 0
    right = len(lists)-1
    while left < right:
        # 左移动，直至指向偶数
        if lists[left] % 2 == 1 and left < right:
            left += 1
        # 右移动，直至指向奇数
        if lists[right] % 2 == 0 and left < right:
            right -= 1
        # 左右交换
        if left < right:
            lists[left], lists[right] = lists[right], lists[left]

    return lists

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print ReOrderArray1(arr)
    print ReOrderArray2(arr)