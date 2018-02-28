# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想： 统计数字
"""
class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        count = 0

        for number in range(n+1):
            while number/10:
                if number % 10 == k:
                    count += 1
                number /= 10

            if number == k:
                count += 1

        return count

if __name__ == '__main__':
    print Solution().digitCounts(1, 12)