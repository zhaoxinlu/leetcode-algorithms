# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-16
算法思想： 爬楼梯--动态规划
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 1 or n == 2:
            return n
        elif n <= 0:
            return 0
        else:
            dp = [0] * (n + 1)
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n+1):
                dp[i] = dp[i-2] + dp[i-1]

        return dp[n]

if __name__ == '__main__':
    print Solution().climbStairs(10)