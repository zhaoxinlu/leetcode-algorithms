# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 更新二进制位
"""
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        # write your code here
        """
        先将N的i到j位清零和把M向右移动i位，然后将N与上M就是所求的答案。
        :param n:
        :param m:
        :param i:
        :param j:
        :return:
        for k in range(i, j+1):
            n &= ~(1 << k)

        m = (m << i)
        return n | m
        """
        a = []
        for k in range(32):
            a.append(n % 2)
            n = n / 2

        for k in range(i, j+1):
            a[k] = m % 2
            m /= 2

        n = 0
        for k in range(31):
            if a[k] == 1:
                n |= (1 << k)

        if a[31] == 1:
            n -= 1 << 31

        return n

if __name__ == '__main__':
    print Solution().updateBits(-521, 0, 31, 31)