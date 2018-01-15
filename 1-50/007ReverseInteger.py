# -*-coding: utf-8 -*-
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            y = int(str(x)[::-1])
        else:
            y = -1 * int(str(-x)[::-1])

        if y > 2 ** 31-1 or y < -2 ** 31:
            y = 0

        return y


if __name__ == '__main__':
    print Solution().reverse(1563847412)