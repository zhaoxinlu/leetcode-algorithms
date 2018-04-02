# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-23
算法思想：贪心策略
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == None or len(height) < 2:
            return 0

        start = 0
        end = len(height) - 1
        maxArea = 0
        while start < end:
            tmpArea = (end-start) * min(height[start], height[end])
            if tmpArea > maxArea:
                maxArea = tmpArea

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxArea

if __name__ == '__main__':
    height = [5, 2, 3, 11, 8]
    print Solution().maxArea(height)