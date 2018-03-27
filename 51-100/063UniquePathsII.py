# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：不同路径II--动态规划
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for i in range(rows)]

        for i in range(rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(cols):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[rows-1][cols-1]

if __name__ == '__main__':
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    print Solution().uniquePathsWithObstacles(arr)