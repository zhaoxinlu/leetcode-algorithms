# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 三数之和
"""
class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if len(numbers) <= 2:
            return []

        result = []
        numbers.sort()

        for i in range(len(numbers)-2):
            left = i + 1
            right = len(numbers)-1
            while left < right:
                val = numbers[i] + numbers[left] + numbers[right]
                if val == 0 and [numbers[i], numbers[left], numbers[right]] not in result:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1

        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, 4]
    print Solution().threeSum(nums)