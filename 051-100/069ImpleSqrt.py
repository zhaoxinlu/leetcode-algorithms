# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：实现sqrt()--二分查找
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x

        low = 1
        high = x/2+1

        while low<high:
            mid = low + (high-low) / 2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid + 1
            else:
                high = mid

        return low-1

if __name__ == '__main__':
    print Solution().mySqrt(4)