# -*- coding: utf-8 -*-
"""
Editor: Zhao xinlu
School: BUPT
Date: 2018-03-14
算法思想： 带重复元素的子集--回溯法/深度优先搜索
"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        self.results = []
        self.DFS(nums, 0, [])
        return self.results

    def DFS(self, nums, m, tmplist):
        self.results.append(tmplist[:])
        for i in range(m, len(nums)):
            if i != m and nums[i] == nums[i-1]:
                continue
            tmplist.append(nums[i])
            self.DFS(nums, i + 1, tmplist)
            tmplist.pop()

if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 2, 2])