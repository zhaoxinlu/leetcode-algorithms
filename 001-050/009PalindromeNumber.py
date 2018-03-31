# -*-coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print Solution().isPalindrome(-2147483648)