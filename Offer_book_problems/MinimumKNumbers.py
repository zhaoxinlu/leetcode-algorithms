# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-18
Function: 前k个数--堆排序
"""
class Solution:
    def GetLeastNumbers(self, tinput, k):
        """
            构建小顶堆，堆降序，前K小数
        :param tinput:
        :param k:
        :return:
        """
        if not tinput or k <= 0:
            return []
        size = len(tinput)
        if k > size:
            return []

        self.bulidLittleHeap(tinput, size)
        result = []
        for i in range(k):
            result.append(tinput[0])
            tinput[0] = tinput[size-1]
            size -= 1
            self.adjustLittleHeap(tinput, 0, size)
        return result

    def bulidLittleHeap(self, nums, size):
        if not nums:
            return
        for i in range(size/2-1, -1, -1):
            self.adjustLittleHeap(nums, i, size)

    def adjustLittleHeap(self, nums, i, size):
        if i < size/2:
            left = 2*i+1
            right = left+1
            smaller = i
            if left < size and nums[smaller] > nums[left]:
                smaller = left
            if right < size and nums[smaller] > nums[right]:
                smaller = right
            if smaller != i:
                nums[smaller], nums[i] = nums[i], nums[smaller]
                self.adjustLittleHeap(nums, smaller, size)

    def heapSortDESC(self, nums):
        if not nums:
            return []
        size = len(nums)
        self.bulidLittleHeap(nums, size)
        for i in range(size-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustLittleHeap(nums, 0, i)

        return nums

##############################分隔符######################################

    def buildHeap(self, nums, size):
        """
            构造大顶堆，堆升序，前K大数
        :param nums:
        :param size:
        :return:
        """
        if not nums:
            return
        for i in range(size/2-1, -1, -1):
            self.adjustHeap(nums, i, size)

    def adjustHeap(self, nums, i, size):
        if i < size/2:
            left = 2*i+1
            right = left+1
            larger = i
            if left < size and nums[larger] < nums[left]:
                larger = left
            if right < size and nums[larger] < nums[right]:
                larger = right
            if larger != i:
                nums[larger], nums[i] = nums[i], nums[larger]
                self.adjustHeap(nums, larger, size)

    def heapSort(self, nums):
        if not nums:
            return []
        size = len(nums)
        self.buildHeap(nums, size)
        for i in range(size-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustHeap(nums, 0, i)

        return nums

    def getLArgestKNumbers(self, nums, k):
        size = len(nums)
        self.buildHeap(nums, size)
        result = []
        for i in range(k):
            result.append(nums[0])
            nums[0] = nums[size-1]
            size -= 1
            self.adjustHeap(nums, 0, size)
        return result

if __name__ == '__main__':
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    #print Solution().heapSort(nums)
    #print Solution().getLArgestKNumbers(nums, 4)
    print Solution().heapSortDESC(nums)
    print Solution().GetLeastNumbers(nums, 4)