# -*- coding: utf-8 -*-
"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        双指针
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i

if __name__ == '__main__':
    print Solution().removeElement([3, 2, 2, 1], 3)