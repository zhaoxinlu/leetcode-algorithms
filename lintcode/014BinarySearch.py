# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想： 二分查找 && 查找到target第一次出现的下标
"""
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                while nums[mid] == target:
                    mid -= 1
                    # 查找到target第一次出现的下标
                return mid+1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5]
    print Solution().binarySearch(arr, 3)