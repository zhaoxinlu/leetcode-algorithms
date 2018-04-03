# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：杨辉三角Pascal's Triangle II
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        创建一个元素数量与最后结果相同的数组，假设参数为4:
            [1,0,0,0,0]
        从最后一个元素开始，本元素等于本元素和前一个相加，
            [1,1,0,0,0]
            [1,2,1,0,0]
            [1,3,3,1,0]
            [1,4,6,4,1]
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex+1)
        result[0] = 1

        for i in range(1, rowIndex+1):
            for j in range(rowIndex, 0, -1):
                result[j] = result[j] + result[j-1]

        return result

if __name__ == '__main__':
    r = 4
    print Solution().getRow(r)