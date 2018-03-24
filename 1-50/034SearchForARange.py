# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：在旋转排序数组中搜索
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        if nums == None or len(nums) < 1:
            return result

        result[0] = self.searchRangeLeft(nums, target)
        result[1] = self.searchRangeRight(nums, target)

        return result

    def searchRangeLeft(self, nums, target):
        left = 0
        right = len(nums)-1

        #########Action!##########
        if nums[0] == target:
            return 0

        while left<=right:
            mid = left + (right-left) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid-1] != target:
                    return mid
                else:
                    right = mid - 1

        return -1

    def searchRangeRight(self, nums, target):
        left = 0
        right = len(nums)-1

        #########Action!##########
        if nums[right] == target:
            return right

        while left <= right:
            mid = left + (right-left) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid+1] != target:
                    return mid
                else:
                    left = mid + 1

        return -1

if __name__ == '__main__':
    print Solution().searchRange([5, 5], 5)