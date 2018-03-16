# -*- coding: utf-8 -*-
"""
Editor: Zhao xinlu
School: BUPT
Date: 2018-03-14
算法思想： 带重复元素的排列--回溯法/深度优先搜索
"""
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        self.results = []
        used = [False] * len(nums)
        self.DFS(nums, [], used)
        return self.results

    def DFS(self, nums, tmplist, used):
        if len(tmplist) == len(nums):
            self.results.append(tmplist[:])
            return
        else:
            for i in range(0, len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and used[i-1] != False:
                    continue
                used[i] = True
                tmplist.append(nums[i])
                self.DFS(nums, tmplist, used)
                used[i] = False
                tmplist.pop()

if __name__ == '__main__':
    nums = [1, 1, 2]
    print Solution().permuteUnique(nums)