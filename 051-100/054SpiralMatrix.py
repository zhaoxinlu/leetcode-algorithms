# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-26
算法思想：螺旋遍历，设置边界
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) == 0:
            return []

        result = []
        rowStart = 0
        rowEnd = len(matrix)-1
        colStart = 0
        colEnd = len(matrix[0])-1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                result.append(matrix[rowStart][i])
            rowStart += 1
            if rowEnd < rowStart:
                break

            for i in range(rowStart, rowEnd+1):
                result.append(matrix[i][colEnd])
            colEnd -= 1
            if colEnd < colStart:
                break

            for i in range(colEnd, colStart-1, -1):
                result.append(matrix[rowEnd][i])
            rowEnd -= 1
            if rowStart > rowEnd:
                break

            for i in range(rowEnd, rowStart-1, -1):
                result.append(matrix[i][colStart])
            colStart += 1
            if colStart > colEnd:
                break

        return result

if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    print Solution().spiralOrder(mat)