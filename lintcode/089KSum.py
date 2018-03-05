# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： k数和--动态规划：dp[y][z]代表 y个数之和为 z 的方案个数。
    时间复杂度  O（n*k*target）， 空间复杂度 O（k*target）
"""
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        dp = [[0] * (target+1) for i in range(k+1)]
        dp[0][0] = 1
        for i in range(len(A)):
            for j in range(k, 0, -1):
                for t in range(target, A[i]-1, -1):
                    dp[j][t] += dp[j - 1][t - A[i]]

        return dp[k][target]

if __name__ == '__main__':
    print Solution().kSum([1, 2, 3, 4], k=2, target=5)