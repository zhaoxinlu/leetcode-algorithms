# -*- coding: utf-8 -*-
"""
Author: Zhao Xinlu
School: BUPT
Date: 2018-01-15
Function: Some different searching algorithms and its performance
"""

def Simple_search(lists, key):
    '''
    Simple_search: 数据不排序的线性查找，遍历数据元素;
    性能：
        时间复杂度：O(n)
    :param lists: search list
    :param key: the value of key
    :return: the key's location in the list
    '''
    length = len(lists)
    for i in range(0, length):
        if lists[i] == key:
            return i
    return False

def Binary_search(lists, key):
    '''
    Binary search(二分查找):在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。
    性能：
        时间复杂度：O(logn)
    :param lists: search list
    :param key: the value of key
    :return: the key's location in the list
    '''
    length = len(lists)
    low = 0
    high = length - 1
    while low < high:
        mid = int((low + high) / 2)
        # mid = low + 1/2 * (high - low)
        if lists[mid] > key:
            high = mid - 1
        elif lists[mid] < key:
            low = mid + 1
        else:
            return mid

    return False

def Binary_search2(lists, key, low, high):
    '''
    Binary search 2(二分查找的递归实现)
    :param lists: search list
    :param key: the value of key
    :param low:
    :param high:
    :return: the key's location in the list
    '''
    mid = int((low + high) / 2)
    if lists[mid] == key:
        return mid
    elif lists[mid] < key:
        return Binary_search2(lists, key, mid+1, high)
    else:
        return Binary_search2(lists, key, low, mid-1)

def Binary_search_plus(lists, key):
    '''
    Binary search plus(插值查找):二分查找的优化
            对半过滤还不够狠，要是每次都排除十分之九的数据岂不是更好？选择这个值就是关键问题
    :param lists: search list
    :param key: the value of key
    :return: the key's location in the list
    '''
    length = len(lists)
    low = 0
    high = length - 1
    while low < high:
        mid = low + int((high - low) * (key - lists[low]) / (lists[high] - lists[low]))
        # 插值的核心公式： value = (key - list[low])/(list[high] - list[low])
        if lists[mid] > key:
            high = mid - 1
        elif lists[mid] < key:
            low = mid + 1
        else:
            return mid

    return False

def Fibonacci_search(lists, key):
    '''
    Fibonacci search(斐波那契查找):利用斐波那契数列的性质，黄金分割的原理来确定mid的位置.
    性能：
        时间复杂的：O(logn)
    :param lists: search list
    :param key: the value of search key
    :return: the key's location in the list
    '''
    # 需要一个现成的斐波那契列表, 其最大元素的值必须超过查找表中元素个数的数值。
    FibonacciList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                     233, 377, 610, 987, 1597, 2584, 4181, 6765,
                     10946, 17711, 28657, 46368]
    length = len(lists)
    low = 0
    high = length - 1

    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-high决定
    k = 0
    while high > FibonacciList[k] - 1:
        k += 1
    print k
    i = high
    while FibonacciList[k] - 1 > i:
        lists.append(lists[high])
        i += 1
    print lists

    # 算法主逻辑
    while low <= high:
        if k < 2:
            mid = low
        else:
            mid = low + FibonacciList[k] - 1
            # 利用斐波那契数列来找寻下一个要比较的关键字的位置

        if key < lists[mid]:
            high = mid - 1
            k -= 1
        elif key > lists[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                return mid
            else:
                return high

    return False

if __name__ == '__main__':
    key = 7
    TestList1 = [3, 6, 5, 9, 7, 1, 8, 2, 4]
    TestList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    TestList3 = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    # result = Simple_search(TestList1, key)
    # result = Binary_search(TestList2, key)
    # result = Binary_search2(TestList2, key, 0, len(TestList2))
    # result = Binary_search_plus(TestList2, key)
    result = Fibonacci_search(TestList3, key=444)
    print "Key's location of the list is : lists[", result, "]"