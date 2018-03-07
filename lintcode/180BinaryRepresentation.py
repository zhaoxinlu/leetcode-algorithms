# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 二进制表示
"""
class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binaryRepresentation(self, n):
        # write your code here
        """
        将n转化为整数部分与小数部分，分别转化成字符串形式再相加.
        :param n:
        :return:
        """
        integer, decimal = str(n).split('.')
        integer = int(integer)
        decimal = float('0.'+decimal)

        interger_to_2str = str(bin(integer))[2:]
        # bin() == 0bxx
        if decimal == 0:
            return interger_to_2str

        decList = []
        for i in range(32):
            decimal *= 2
            decList.append(int(decimal))
            decimal -= int(decimal)
            if decimal == 0:
                break
        decimal_to_str = '.'
        for s in decList:
            decimal_to_str += str(s)

        if len(decimal_to_str) > 32:
            return "ERROR"
        else:
            return interger_to_2str+decimal_to_str

if __name__ == '__main__':
    print Solution().binaryRepresentation(0.5)