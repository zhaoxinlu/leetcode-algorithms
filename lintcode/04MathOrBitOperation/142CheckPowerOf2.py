# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： O(1)时间检测2的幂次--位操作
"""
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        """
        2 = (10)2(10)2 --> 1 = (01)2(01)2 --> 2&1==0
        4 = (100)2(100)2 --> 3 = (011)2(011)2 --> 4&3=0
        8 = (1000)2(1000)2 --> 7 = (0111)2(0111)2 --> 8&7=0
        :param n:
        :return:
        """
        if n < 1:
            return False
        else:
            return (n & (n-1)) == 0

if __name__ == '__main__':
    print Solution().checkPowerOf2(4)