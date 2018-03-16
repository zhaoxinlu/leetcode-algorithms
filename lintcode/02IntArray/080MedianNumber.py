# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 未排序数组的中位数--快排思想
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        if len(nums) < 1 or nums == None:
            return None

        k = (len(nums)+1) / 2

        return self.getMinK(nums, 0, len(nums)-1, k)

    def getMinK(self, nums, left, right, k):
        pos = self.partition(nums, left, right)

        if pos == k - 1:
            return nums[pos]
        elif pos > k - 1:
            return self.getMinK(nums, left, pos-1, k)
        else:
            return self.getMinK(nums, pos+1, right, k)

    def partition(self, nums, left, right):
        low = left
        high = right
        key = nums[low]

        while low < high:
            while low < high and nums[high] >= key:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] <= key:
                low += 1
            nums[high] = nums[low]

            nums[low] = key

        return low

if __name__ == '__main__':
    nums = [-1, -2, -3, -100, -1, -50]
    print Solution().median(nums)