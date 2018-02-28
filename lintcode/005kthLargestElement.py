# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想： 数组第K大元素
    1.进行一次快排（将大的元素放在后半段，小的元素放在前半段）, 假设得到的中轴为p
    2.判断 k -1 == right - p，如果成立，直接输出a[p]，（因为后半段有k - 1个大于a[p]的元素，故a[p]为第K大的元素）
    3.如果 k -1 < right - p， 则第k大的元素在后半段，此时更新left = p + 1，继续进行步骤1
    4.如果 k -1 > right - p， 则第k大的元素在前半段，此时更新right = p - 1, 且 k = k-1-right+p，继续步骤1.
    由于常规快排要得到整体有序的数组，而此方法每次可以去掉“一半”的元素，故实际的复杂度不是o(nlgn), 而是o(n)。
"""
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        return self.kthLargestElem(k, A, 0, len(A) - 1)

    def kthLargestElem(self, k, A, left, right):
        p = self.partition(A, left, right)
        if k - 1 == right - p:
            return A[p]
        elif k - 1 > right - p:
            return self.kthLargestElem(k-1-right+p, A, left, p-1)
        else:
            return self.kthLargestElem(k, A, p+1, right)

    def partition(self, A, left, right):
        low = left
        high = right
        key = A[low]

        while low < high:
            while low < high and A[high] >= key:
                high -= 1
            A[low] = A[high]

            while low < high and A[low] <= key:
                low += 1
            A[high] = A[low]

            A[low] = key

        return low

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print Solution().kthLargestElement(2, arr)