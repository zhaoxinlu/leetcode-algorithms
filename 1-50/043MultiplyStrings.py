# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：字符串相乘
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            return self.multiply(num2, num1)

        num1 = num1[::-1]
        num2 = num2[::-1]
        arr = [0] * (len(num1)+len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] / 10
            if i < len(arr)-1:
                arr[i+1] += carry
            ans.insert(0, str(digit))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]

        return ''.join(ans)