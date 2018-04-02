# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：三角形Triangle
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)

        for i in range(rows-2, -1, -1):
            for j in range(0, len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print Solution().minimumTotal(triangle=tri)