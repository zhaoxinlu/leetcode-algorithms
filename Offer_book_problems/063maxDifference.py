# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 数组中所有数对的最大差值
"""
def MaxDifference(arr):
    """
    数组中所有数对的最大差值
    :param arr:
    :return:
    """
    if arr == None or len(arr) < 2:
        return 0

    minN = arr[0]
    maxDiff = arr[1] - minN

    for i in range(2, len(arr)):
        if arr[i-1] < minN:
            minN = arr[i-1]

        curDiff = arr[i] - minN
        if curDiff > maxDiff:
            maxDiff = curDiff

    return maxDiff

if __name__ == '__main__':
    print MaxDifference([9, 11, 8, 5, 7, 12, 16, 14])