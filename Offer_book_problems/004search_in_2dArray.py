# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-22
Function: 二维数组的查找
    在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
def search_in2dArray(arr, num):
    rows = len(arr)

    row = 0
    col = len(arr[0])-1
    # 比较右上角元素

    while row <= rows and col >= 0:
        if arr[row][col] == num:
            print "The number {} is in array[{}][{}]".format(num, row, col)
            return
        elif arr[row][col] > num:
            col -= 1
        else:
            row += 1

    print "The number {} is not in array!".format(num)
    return

def search_in2dArray2(arr, num):
    rows = len(arr)
    cols = len(arr[0])-1
    # 比较左下角元素
    row = rows-1
    col = 0
    while col <= cols and row >= 0:
        if arr[row][col] == num:
            print "The number {} is in array[{}][{}].".format(num, row, col)
            return
        elif arr[row][col] < num:
            col += 1
        else:
            row -= 1

    print "The number {} is not in array!".format(num)
    return

if __name__ == '__main__':
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    search_in2dArray(arr, 7)
    search_in2dArray2(arr, 5)