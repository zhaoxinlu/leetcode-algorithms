# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 最大数--重写快速排序（O(nlogn)）
"""
class Solution:
    """
    @param: nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        if len(nums) == 0:
            return '0'

        self.quickSort(nums, 0, len(nums)-1)
        result = ''

        for i in range(len(nums)-1, -1, -1):
            result += str(nums[i])

        if nums[len(nums)-1] == 0:
            return '0'
        return result

    def quickSort(self, nums, start, end):
        if start < end:
            left = start
            right = end
            key = nums[start]
            while left < right:
                while left < right and self.helperCompare(nums[right], key) >= 0:
                    right -= 1
                nums[left] = nums[right]
                while left < right and self.helperCompare(nums[left], key) <= 0:
                    left += 1
                nums[right] = nums[left]
            nums[left] = key
            self.quickSort(nums, start, left-1)
            self.quickSort(nums, left+1, end)

    def helperCompare(self, num1, num2):
        s1 = str(num1)
        s2 = str(num2)

        if (s1+s2) > (s2+s1):
            return 1
        elif (s1+s2) < (s2+s1):
            return -1
        else:
            return 0

if __name__ == '__main__':
    nums = [1, 20, 23, 4, 8]
    print Solution().largestNumber(nums)