# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：螺旋遍历
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        rowStart = 0
        rowEnd = n-1
        colStart = 0
        colEnd = n-1
        index = 1

        while index <= n*n:
            for i in range(colStart, colEnd+1):
                matrix[rowStart][i] = index
                index += 1
            rowStart += 1

            for i in range(rowStart, rowEnd+1):
                matrix[i][colEnd] = index
                index += 1
            colEnd -= 1

            for i in range(colEnd, colStart-1, -1):
                matrix[rowEnd][i] = index
                index += 1
            rowEnd -= 1

            for i in range(rowEnd, rowStart-1, -1):
                matrix[i][colStart] = index
                index += 1
            colStart += 1

        return matrix

if __name__ == '__main__':
    print Solution().generateMatrix(3)