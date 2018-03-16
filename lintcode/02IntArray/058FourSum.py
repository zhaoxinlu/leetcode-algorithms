# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 四数之和
"""
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        if len(numbers) < 4:
            return []

        result = []
        numbers.sort()

        for i in range(len(numbers)-3):
            for j in range(i+1, len(numbers)):
                left = j + 1
                right = len(numbers) - 1
                while left < right:
                    val = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if val == target and [numbers[i], numbers[j], numbers[left], numbers[right]] not in result:
                        result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                    elif val < target:
                        left += 1
                    else:
                        right -= 1

        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    print Solution().fourSum(nums, 0)