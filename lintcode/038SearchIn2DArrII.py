# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 搜索二维矩阵 II
"""
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        count = 0

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                count += 1
                row += 1
                col -= 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return count

if __name__ == '__main__':
    mat = [[1, 3, 5, 7], [2, 4, 7, 8], [3, 7, 9, 10]]
    print Solution().searchMatrix(mat, 7)