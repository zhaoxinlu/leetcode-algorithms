# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：全排列II--有相同数字
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.DFS(nums, [], used, result)
        return result

    def DFS(self, nums, tmp, used, result):
        if len(tmp) == len(nums):
            result.append(tmp[:])
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] != False:
                    #当试图将第二个1作为第一个元素添加进结果集时，只要第一个1还没有被使用过，则不可以使用第二个1。
                    continue

                used[i] = True
                tmp.append(nums[i])
                self.DFS(nums, tmp, used, result)
                tmp.pop()
                used[i] = False

if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2])