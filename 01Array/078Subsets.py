# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：子集--回溯
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, m, tmp, result):
        result.append(tmp[:])
        for i in range(m, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, i+1, tmp, result)
            tmp.pop()

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)