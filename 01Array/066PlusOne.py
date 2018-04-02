# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：加一--进位
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp / 10

        if carry == 1:
            digits.insert(0, carry)

        return digits