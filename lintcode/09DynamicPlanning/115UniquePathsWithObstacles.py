# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-20
算法思想： 不同的路径II之有障碍物--动态规划
"""
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[m-1][n-1]

if __name__ == '__main__':
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    print Solution().uniquePathsWithObstacles(arr)