# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-06
算法思想：股票最大差值
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0

        minPrice = prices[0]
        maxProfit = prices[1] - minPrice

        for i in range(2, len(prices)):
            if prices[i-1] < minPrice:
                minPrice = prices[i-1]

            # minPrice = min(prices[:i]) TLE超时

            curProfit = prices[i] - minPrice

            if curProfit > maxProfit:
                maxProfit = curProfit

        return max(maxProfit, 0)

if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    print Solution().maxProfit(p)