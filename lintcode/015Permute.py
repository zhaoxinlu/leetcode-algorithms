# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 全排列
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if (len(nums) <= 1):
            return [nums]
        r = []
        for i in range(len(nums)):
            s = nums[:i] + nums[i + 1:]
            p = self.permute(s)
            for x in p:
                r.append(nums[i:i + 1] + x)
        return r

    def permute1(self, nums):
        # write your code here
        result = []
        self.helper(nums, 0, len(nums), result)
        return result

    def helper(self, nums, left, right, result):
        if left == right:
            result.append(nums)
            ### 有问题
            return
        else:
            for i in range(left, right):
                nums[i], nums[left] = nums[left], nums[i]
                self.helper(nums, left+1, right, result)
                nums[i], nums[left] = nums[left], nums[i]

if __name__ == '__main__':
    print Solution().permute([1, 2, 3])