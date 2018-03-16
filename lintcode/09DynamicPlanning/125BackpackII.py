# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 01背包问题II--最大价值--动态规划
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        dp = [[0] * (m+1) for i in range(len(A)+1)]
        # dp[i][j]表示前i件物品，不超过背包大小j的最大价值

        for i in range(1, len(A)+1):
            for j in range(1, m+1):
                if j - A[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(A)][m]

if __name__ == '__main__':
    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    print Solution().backPackII(10, A, V)