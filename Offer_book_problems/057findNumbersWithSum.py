# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 和为s的数字 && 和为s的连续正数序列
"""
def FindNumbersWithSum(arr, value):
    """
    （一）递增排序arr，在数组中查找两个数，使其和为value
    :param arr:
    :param value:
    :return:
    """
    result = []
    left = 0
    right = len(arr) - 1

    while left<right:
        if arr[left] + arr[right] == value:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif arr[left] + arr[right] < value:
            left += 1
        else:
            right -= 1

    return result

def FindContinuousSequence(value):
    """
    （二）输入正数value，打印所有和为value的连续正数序列
    :param value:
    :return:
    """
    if value < 3:
        return False

    small = 1
    big = 2
    mid = (1 + value) / 2
    curSum = small + big
    results = []

    while small < mid:
        if curSum == value:
            r = PrintContinuousSequence(small, big)
            results.append(r)

        while curSum > value and small < mid:
            curSum -= small
            small += 1

            if curSum == value:
                r = PrintContinuousSequence(small, big)
                results.append(r)

        big += 1
        curSum += big

    return results

def PrintContinuousSequence(small, big):
    result = []

    for i in range(small, big+1):
        result.append(i)

    return result

if __name__ == '__main__':
    print FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15)
    print FindContinuousSequence(15)