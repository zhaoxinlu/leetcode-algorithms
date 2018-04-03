# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：先上下翻转，在沿对角线镜像
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == None:
            return None

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows/2):
            for j in range(cols):
                matrix[i][j], matrix[rows-i-1][j] = matrix[rows-i-1][j], matrix[i][j]

        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #return matrix