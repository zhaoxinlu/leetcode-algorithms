# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-05
算法思想：学习python中堆数据结构heapq
"""
import heapq

def ChangeListToHeap(listA):
    heapq.heapify(listA) # 将list转换为堆

    heapA = [] # 建立空堆

    ## (minN =) heapq.heappop(listA) # 弹出堆中的最小元素

    ## heapq.heappush(heapA, item) # 往堆中插入一条新的值

    ## item = heapA[0] # 查看堆中最小值, 不弹出

    ## heapq.heapreplace(heap, item) # 删除最小元素值，添加新的元素值

    ## heapq.merge(...) # 合并多个堆

    ## heapq.nlargest(n, heap) # 查询堆中的最大元素，n表示查询元素个数

    ## heapq.nsmallest(n, heap) # 查询堆中的最小元素，n表示查询元素个数

    while listA:
        heapA.append(heapq.heappop(listA))

    return heapA

if __name__ == '__main__':
    nums = [3, 2, 1, 4, 5]
    heapq.heapify(nums)
    print nums
    print heapq.nlargest(3, nums) # [5, 4, 3]