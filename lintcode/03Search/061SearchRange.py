# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 搜索区间
    二分查找左右边界，O（logn）
"""
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        result = [-1, -1]
        if A == None or len(A) == 0:
            return result

        result[0] = self.searchRangeLeft(A, target)
        result[1] = self.searchRangeRight(A, target)

        return result

    def searchRangeLeft(self, A, target):
        left = 0
        right = len(A) - 1

        if A[0] == target:
            return 0

        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                if A[mid-1] != target:
                    return mid
                else:
                    right = mid - 1

        return -1

    def searchRangeRight(self, A, target):
        left = 0
        right = len(A) - 1

        if A[right] == target:
            return right

        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                if A[mid+1] != target:
                    return mid
                else:
                    left = mid + 1

        return -1


if __name__ == '__main__':
    A = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    print Solution().searchRange(A, target)