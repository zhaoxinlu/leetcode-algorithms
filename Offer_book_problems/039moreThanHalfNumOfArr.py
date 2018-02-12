# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-12
Function: 数组中出现次数超过一半的数字, 时间复杂度为O(n)
"""
def checkInvalidArray(arr):
    """
    辅助检查函数，判断输入的数组是否有效
    :param arr:
    :return:
    """
    invalidFlag = False
    if len(arr) <= 0 or arr == None:
        invalidFlag = True

    return invalidFlag

def checkMoreThanHalf(arr, value):
    """
    检查值出现次数是否大于数组长度的一半
    :param arr:
    :param value:
    :return:
    """
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == value:
            count += 1

    isMoreThanHalf = True
    if count * 2 <= len(arr):
        isMoreThanHalf = False

    return isMoreThanHalf

def MoreThanHalfNumOfArr(arr):
    """
    主函数，根据数组的特点寻找次数超过一半的数字，时间复杂度为O(n)
    :param arr:
    :return:
    """
    if checkInvalidArray(arr):
        return False

    result = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if count == 0:
            result = arr[i]
            count = 1
        elif arr[i] == result:
            count += 1
        else:
            count -= 1

    if not checkMoreThanHalf(arr, result):
        return None

    return result

if __name__ == '__main__':
    # Test
    print MoreThanHalfNumOfArr([1, 2, 3, 2, 2, 5, 4, 2, 2])