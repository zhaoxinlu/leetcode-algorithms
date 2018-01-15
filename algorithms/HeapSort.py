# -*- coding: utf-8 -*-
"""
Heap sort(堆排序)-MAX: 初始时把要排序的数的序列看作是一棵顺序存储的二叉树，调整它们的存储序，使之成为一个堆，这时堆的根节点的数最大;
            然后将根节点与堆的最后一个节点交换。然后对前面(n-1)个数重新调整使之成为堆;
            依此类推，直到只有两个节点的堆，并对 它们作交换，最后得到有n个节点的有序序列。
            从算法描述来看，堆排序需要两个过程，一是建立堆，二是堆顶与堆的最后一个元素交换位置。
            所以堆排序有两个函数组成。一是建堆的渗透函数，二是反复调用渗透函数实现排序的函数。
    1.创建最大堆:将堆所有数据重新排序，使其成为最大堆
    2.最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
    3.堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算
性能：
    时间复杂度：O(nlog₂n)
    空间复杂度：O(1)
    稳定性：不稳定
"""

def Heap_adjust(lists, parent, size):
    lchild = 2 * parent + 1
    rchild = 2 * parent + 2
    maxN = parent
    while parent < size / 2:
        if lchild < size and lists[lchild] > lists[maxN]:
            maxN = lchild
        if rchild < size and lists[rchild] > lists[maxN]:
            maxN = rchild
        if maxN != parent:
            lists[maxN], lists[parent] = lists[parent], lists[maxN]
            Heap_adjust(lists, maxN, size)

def Heap_build(lists, size):
    for i in range(0, (size/2))[::-1]:
        print i
        Heap_adjust(lists, i, size)

def Heap_sort(lists):
    '''

    :param lists:
    :return:
    '''

    size = len(lists)
    Heap_build(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        Heap_adjust(lists, 0, i)

    return lists