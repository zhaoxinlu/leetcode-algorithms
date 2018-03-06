# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 最小调整代价--动态规划
"""
class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        dp = [[2147483647] * 101 for i in range(len(A)+1)]
        """
        dp中第i行对应A[i-1]。对于每个数A[i]，调整后的结果有100种，用dp[i][j]表示数字A[i]调整为j的最小代价。
        对于每个dp[i][j]，A[i-1]调整到k的代价加上A[i]调整到j的最小代价即为dp[i][j]的代价。
        而k又有100种选择，对于j，当|j-k|的绝对值不大于target时，代价最小，当前dp[i][j]为dp[i-1][k] +(j-A[i-1])，dp[i][j]保留所有可能代价中的最小代价。

        最后，dp[n][0~100]中的最小代价即为对整个数组调整后的最下代价。
        """

        for j in range(101):
            dp[0][j] = 0

        for i in range(1, len(A)+1):
            for j in range(101):
                for k in range(101):
                    if abs(j-k) <= target:
                        dp[i][j] = min(dp[i][j], dp[i-1][k]+abs(A[i-1]-k))

        return min(dp[len(A)])

if __name__ == '__main__':
    A = [1, 4, 2, 3]
    target = 1
    print Solution().MinAdjustmentCost(A, target=target)