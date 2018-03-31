# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：二进制相加--进位
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, m, n, result, carry = 1, len(a), len(b), [], 0
        while i <= m or i <= n:
            temp = carry
            if i <= m:
                temp += int(a[-i])
            if i <= n:
                temp += int(b[-i])

            carry = temp / 2
            result.append(str(temp % 2))
            i += 1

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])

if __name__ == '__main__':
    print Solution().addBinary('11', '1')