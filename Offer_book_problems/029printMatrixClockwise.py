# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-30
Function: 顺时针打印矩阵
"""
def printMatrixClockWisely(matrix):
    """
    按圈循环打印矩阵
    :param matrix:
    :return:
    """
    rows = len(matrix)
    cols = len(matrix[0])

    if matrix == None or rows <= 0 or cols <= 0:
        return None

    start = 0
    elems = []

    while cols > start * 2 and rows > start * 2:
        # start控制打印的圈
        printMatrixInCircle(matrix, cols, rows, start, elems)
        start += 1

    return elems

def printMatrixInCircle(matrix, cols, rows, start, elems):
    """
    按矩阵的圈打印，分四步：从左到右，上到下，右到左，下到上（注意边界判断）
    :param matrix:
    :param cols:
    :param rows:
    :param start:
    :param elems:
    :return:
    """
    endX = cols - 1 - start
    endY = rows - 1 - start

    for i in range(start, endX+1):
        elems.append(matrix[start][i])

    if start < endY:
        for i in range(start+1, endY+1):
            elems.append(matrix[i][endX])

    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            elems.append(matrix[endY][i])

    if start < endX and start < endY - 1:
        for i in range(endY-1, start, -1):
            elems.append(matrix[i][start])

if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print printMatrixClockWisely(matrix=mat)