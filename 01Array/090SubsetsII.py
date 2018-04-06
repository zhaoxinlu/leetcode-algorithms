# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-06
算法思想：有重复元素的子集--回溯
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## 先排序
        nums.sort()
        result = []
        self.subsetsWithDupDFS(nums, 0, [], result)
        return result

    def subsetsWithDupDFS(self, nums, start, tmp, result):
        result.append(tmp[:])
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.subsetsWithDupDFS(nums, i+1, tmp, result)
            tmp.pop()

if __name__ == '__main__':
    nums = [1, 2, 2, 2]
    print Solution().subsetsWithDup(nums)