# -*- coding: utf-8 -*-
"""
Implement pow(x, n)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0.0
        elif n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -1 * n)
        else:
            tmp = self.myPow(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * x

if __name__ == '__main__':
    print Solution().myPow(1, 0)