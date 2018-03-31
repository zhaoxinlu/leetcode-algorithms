# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1

        return i+1

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2, 2, 2, 3, 4, 4, 5])