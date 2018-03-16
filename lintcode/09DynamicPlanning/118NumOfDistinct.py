# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-16
算法思想： 不同的子序列--动态规划
"""
class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        if S == None or T == None:
            return 0

        dp = [[0] * (len(T)+1) for i in range(len(S)+1)]

        for i in range(0, len(S)+1):
            dp[i][0] = 1

        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                if S[i-1] != T[j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        return dp[len(S)][len(T)]

if __name__ == '__main__':
    S = 'rabbbit'
    T = 'rabbit'
    print Solution().numDistinct(S, T)