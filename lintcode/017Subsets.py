# -*- coding: utf-8 -*-
"""
Editor: 九章算法
School: BUPT
Date: 2018-03-12
算法思想： 子集
"""
class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        self.result = []
        self.search(sorted(nums), [], 0)
        return self.result

    def search(self, nums, S, index):
        if index == len(nums):
            self.result.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)