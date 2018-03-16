# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 将整数A转换为B--位操作
"""
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        """
        1. 将两个数按位异或;
        2. 统计异或结果中1的个数.
        :param a:
        :param b:
        :return:
        """
        c = a ^ b
        count = 0
        flag = 1

        for i in range(32):
            if c & flag != 0:
                count += 1
            flag = (flag << 1)

        return count

if __name__ == '__main__':
    print Solution().bitSwapRequired(31, 14)
