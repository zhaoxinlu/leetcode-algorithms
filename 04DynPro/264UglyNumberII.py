# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-24
Function: 寻找第N大丑数II--动态规划
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        uglyNumbers = [1]
        i2, i3, i5 = 0, 0, 0
        while len(uglyNumbers) < n:
            tmp = min(uglyNumbers[i2]*2, uglyNumbers[i3]*3, uglyNumbers[i5]*5)
            uglyNumbers.append(tmp)
            if tmp == uglyNumbers[i2]*2:
                i2 += 1
            if tmp == uglyNumbers[i3]*3:
                i3 += 1
            if tmp == uglyNumbers[i5]*5:
                i5 += 1
        return uglyNumbers[n-1]

if __name__ == '__main__':
    print Solution().nthUglyNumber(5)