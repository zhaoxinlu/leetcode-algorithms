# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 不同的二叉查找树
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n <= 0:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[n]

if __name__ == '__main__':
    print Solution().numTrees(3)