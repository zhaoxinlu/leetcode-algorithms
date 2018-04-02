# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-26
算法思想：贪心--跳跃游戏
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = 0
        curSum = 0

        while idx<=curSum:
            curSum = max(curSum, nums[idx]+idx)
            idx += 1
            if curSum >= len(nums)-1:
                return True

        return False

if __name__ == '__main__':
    print Solution().canJump([3, 2, 1, 0, 4])