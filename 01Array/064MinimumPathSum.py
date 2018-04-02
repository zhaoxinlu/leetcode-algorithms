# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：最小路径和--动态规划
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for i in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][cols-1]

if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print Solution().minPathSum(grid)