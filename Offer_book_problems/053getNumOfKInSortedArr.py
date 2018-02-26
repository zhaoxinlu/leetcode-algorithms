# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 数字在排序数组中出现的次数
        借助二分查找的方法，时间复杂度：O(logn)
"""
def getFirstK(arr, value, start, end):
    if start > end:
        return -1

    midIndex = (start + end) / 2
    midValue = arr[midIndex]

    if midValue == value:
        if (midIndex > 0 and arr[midIndex-1] != value) or midIndex == 0:
            return midIndex
        else:
            end = midIndex - 1
    elif midValue > value:
        end = midIndex - 1
    else:
        start = midIndex + 1

    return getFirstK(arr, value, start, end)

def getLastK(arr, value, start, end):
    if start > end:
        return -1

    midIndex = (start + end) / 2
    midValue = arr[midIndex]

    if midValue == value:
        if (midIndex < (len(arr)-1) and arr[midIndex + 1] != value) or midIndex == (len(arr)-1):
            return midIndex
        else:
            start = midIndex + 1
    elif midValue > value:
        end = midIndex - 1
    else:
        start = midIndex + 1

    return getLastK(arr, value, start, end)

def getNumOfKInSortedArr(arr, value):
    result = 0

    if arr != None and len(arr) > 0:
        first = getFirstK(arr, value, 0, len(arr)-1)
        last = getLastK(arr, value, 0, len(arr)-1)

        if first > -1 and last > -1:
            result = last - first + 1

    return result

if __name__ == '__main__':
    print getNumOfKInSortedArr([1, 2, 3, 3, 3, 3, 4, 5], 3)