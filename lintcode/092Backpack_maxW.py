# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 01背包问题I--最大空间--动态规划
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        dp = [0] * (m+1)
        # 一维数组 dp[i] 记录所有物品在背包大小为 j 的条件下，最多可以装满的空间

        for i in range(len(A)):
            for j in range(m, 0, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]]+A[i])

        return dp[m]

if __name__ == '__main__':
    A = [2, 3, 5, 7]
    m = 12
    print Solution().backPack(m, A)