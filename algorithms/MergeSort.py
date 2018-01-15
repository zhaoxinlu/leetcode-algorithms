# -*- coding: utf-8 -*-
"""
归并（Merge）排序：是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。
        然后再把有序子序列合并为整体有序序列。
    1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
    2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
    3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
    4.重复步骤3直到某一指针到达序列尾
    5.将另一序列剩下的所有元素直接复制到合并序列尾
性能：
    时间复杂度：O(nlog₂n)
    空间复杂度：O(1)
    稳定性：稳定
"""
def Merge(left, right):
    i, j = 0, 0
    MergeList = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            MergeList.append(left[i])
            i += 1
        else:
            MergeList.append(right[j])
            j += 1

    while i < len(left):
        MergeList.append(left[i])
        i += 1
    while j < len(right):
        MergeList.append(right[j])
        j += 1

    return MergeList

def Merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) / 2
    left = Merge_sort(lists[:middle])
    right = Merge_sort(lists[middle:])
    return Merge(left, right)