# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 搜索旋转数组II--有重复元素
"""
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                return True

            if A[mid] > A[left]:
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[left]:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1

        return False

if __name__ == '__main__':
    A = [4, 5, 5, 7, 1, 2, 3]
    target = 5
    print Solution().search(A, target)