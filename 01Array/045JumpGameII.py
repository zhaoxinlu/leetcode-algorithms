# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-04
算法思想：跳跃游戏II--贪心
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0 # 上一跳所能到达的最远距离
        curMax = 0 # 当前一跳可达最远距离
        step = 0 # 当前跳数

        for i in range(0, len(nums)):
            if i > curMax:
                return -1

            if i > last:
                last = curMax
                step += 1

            curMax = max(curMax, nums[i]+i)

        return step