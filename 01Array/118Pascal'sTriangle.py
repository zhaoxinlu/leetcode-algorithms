# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-06
算法思想：杨辉三角
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(0, numRows):
            result.append([1])
            for j in range(1, i+1):
                if j != i:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
                else:
                    result[i].append(1)

        return result

if __name__ == '__main__':
    n = 5
    print Solution().generate(n)