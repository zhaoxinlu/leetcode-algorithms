# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想： 旋转字符串，按照偏移量
    利用python的切片(数组特性)
"""
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if not str: return
        if not offset: return

        offset = offset % len(str)

        r = len(str) - offset

        """
            for i in range(offset):
                s = str.pop()
                str.insert(0, s)
        """
        return str[r:len(str)]+str[0:r]


if __name__ == '__main__':
    str = 'abcdefg'
    print Solution().rotateString(str, 3)