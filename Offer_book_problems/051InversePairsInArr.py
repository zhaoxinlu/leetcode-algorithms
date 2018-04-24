# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-17
Function: 数组中的逆序对--基于归并排序
"""
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data or len(data) <= 0:
            return 0
        helpArr, countIPs = self.merge(data, 0)
        return countIPs

    def merge(self, data, countIPs):
        if len(data) <= 1:
            return data, 0
        mid = len(data) / 2
        left, countLeft = self.merge(data[:mid], countIPs)
        right, countRight = self.merge(data[mid:], countIPs)
        len_l, len_r = len(left), len(right)
        helperArr = [0] * (len_l+len_r)
        helperArrIndex = len(helperArr)-1
        leftIndex, rightIndex = len_l-1, len_r-1
        count = 0
        while leftIndex >= 0 and rightIndex >= 0:
            if left[leftIndex] > right[rightIndex]:
                count += (rightIndex+1)
                helperArr[helperArrIndex] = left[leftIndex]
                helperArrIndex -= 1
                leftIndex -= 1
            else:
                helperArr[helperArrIndex] = right[rightIndex]
                helperArrIndex -= 1
                rightIndex -= 1

        while leftIndex >= 0:
            helperArr[helperArrIndex] = left[leftIndex]
            helperArrIndex -= 1
            leftIndex -= 1

        while rightIndex >= 0:
            helperArr[helperArrIndex] = right[rightIndex]
            helperArrIndex -= 1
            rightIndex -= 1

        return helperArr, (count+countLeft+countRight) % 1000000007

if __name__ == '__main__':
    arr = [7, 5, 6, 4]
    print Solution().InversePairs(arr)