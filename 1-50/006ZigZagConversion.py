# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-23
算法思想： 字符串画图找规律
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == None or len(s) == 0 or numRows <= 0:
            return ""
        if numRows == 1 or numRows >= len(s):
            return s
        result = []
        for i in range(numRows):
            start = i
            result.append(s[i])

            j = 1
            while start < len(s):
                if i == 0 or i == numRows-1:
                    start = start + 2*numRows - 2
                elif j % 2 == 1:
                    start = start + 2 * (numRows-i-1)
                else:
                    start = start + 2 * i

                if start < len(s):
                    result.append(s[start])

                j += 1

        return ''.join(result)

if __name__ == '__main__':
    print Solution().convert("PAYPALISHIRING", 4)