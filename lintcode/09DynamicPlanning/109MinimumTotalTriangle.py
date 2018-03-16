# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-16
算法思想： 爬楼梯--动态规划
"""
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        length = len(triangle)

        if triangle == None:
            return None
        elif length == 1:
            return triangle[0][0]
        else:
            for i in range(length-2, -1, -1):
                for j in range(len(triangle[i])):
                    tmp = min(triangle[i+1][j], triangle[i+1][j+1])
                    triangle[i][j] += tmp

        return triangle[0][0]

if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print Solution().minimumTotal(tri)