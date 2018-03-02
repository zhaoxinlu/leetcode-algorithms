# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 划分数组
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums)-1

        while left <= right:
            while left <= right and nums[right] >= k:
                right -= 1
            while left <= right and nums[left] < k:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

if __name__ == '__main__':
    # nums = [7, 7, 9, 8, 6, 6, 8, 7, 9, 8, 6, 6] # k=10
    nums = [3, 2, 2, 1]
    print Solution().partitionArray(nums, 2)