# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 旋转数组的最小数字
"""
def minNumInRotatedArray(lists):
    """
    借助二分查找思想查找旋转数组中最小值
    :param lists:
    :return:
    """
    left = 0
    right = len(lists) - 1
    mid = left

    while lists[left] >= lists[right]:
        if right-left == 1:
            mid = right
            break

        mid = (left+right) / 2

        # 如果中间位置的数既等于left位置的数又等于right位置的数
        if lists[mid] == lists[left] and lists[mid] == lists[right]:
            return minInOrder(lists)

        if lists[mid] >= lists[left]:
            left = mid
        else:
            right = mid

    return lists[mid]

def minInOrder(lists):
    """
    顺序查找最小值
    :param lists:
    :return:
    """
    minNum = lists[0]

    for i in range(len(lists)):
        if lists[i] < minNum:
            minNum = lists[i]

    return minNum

if __name__ == '__main__':
    lists = [3, 1, 1, 1, 3]
    print minNumInRotatedArray(lists=lists)