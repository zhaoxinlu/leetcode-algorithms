# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 丑数: 只含素因子2，3，5 的第 n 小的数(包含1)
"""
class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n <= 0:
            return 0
        if n == 1:
            return 1

        uglyNumbers = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            minN = min(uglyNumbers[i2]*2, uglyNumbers[i3]*3, uglyNumbers[i5]*5)
            uglyNumbers.append(minN)
            if minN == uglyNumbers[i2]*2:
                i2 += 1
            if minN == uglyNumbers[i3]*3:
                i3 += 1
            if minN == uglyNumbers[i5]*5:
                i5 += 1

        return uglyNumbers[n-1]

    def isUglyNumber(self, num):
        if num <= 0:
            return False

        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        if num == 1:
            return True
        return False

if __name__ == '__main__':
    print Solution().nthUglyNumber(9)
    print Solution().isUglyNumber(14)