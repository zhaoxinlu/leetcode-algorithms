# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： x的平方根
"""
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        right = 46341 # 防止溢出，设最大上限

        while left <= right:
            mid = left + (right - left) / 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp > x:
                right = mid - 1
            else:
                left = mid + 1

        return right

if __name__ == '__main__':
    print Solution().sqrt(5)