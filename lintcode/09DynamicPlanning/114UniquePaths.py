# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-20
算法思想： 不同的路径--动态规划
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0] * (n) for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

if __name__ == '__main__':
    print Solution().uniquePaths(3, 3)