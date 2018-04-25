# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-25
Function: 2D区域检索--动态规划
"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or len(matrix) == 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0] * (cols+1) for i in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.dp[i][j] = self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1]-self.dp[row2+1][col1]-self.dp[row1][col2+1]+self.dp[row1][col1]