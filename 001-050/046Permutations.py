# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：全排列--回溯，DFS
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.DFS(nums, [], result)
        return result

    def DFS(self, nums, tmp, result):
        if len(tmp) == len(nums):
            result.append(tmp[:])
        else:
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                self.DFS(nums, tmp, result)
                tmp.pop()

if __name__ == '__main__':
    print Solution().permute([1, 2, 3])