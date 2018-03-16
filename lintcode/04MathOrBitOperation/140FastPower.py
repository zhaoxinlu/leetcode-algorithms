# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 快速幂--分治
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        elif n == 1:
            return a % b
        elif n < 0:
            return 0

        tmp = self.fastPower(a, b, n/2)

        if n % 2 == 1:
            return (tmp * tmp * a) % b
        else:
            return (tmp * tmp) % b

if __name__ == '__main__':
    print Solution().fastPower(2, 3, 31)