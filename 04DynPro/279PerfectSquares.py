# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-25
Function: 完全平方和--动态规划
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [100] * (n+1)
        dp[0] = 0
        for i in range(0, n+1):
            j = 1
            while i + j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j += 1

        return dp[n]

if __name__ == '__main__':
    print Solution().numSquares(5)