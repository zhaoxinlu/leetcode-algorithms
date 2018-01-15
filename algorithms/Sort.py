# -*- coding: utf-8 -*-
"""
Author: Zhao Xinlu
School: BUPT
Date: 2018-01-09
Function: Some different sort algorithms and its performance
"""

import math
from HeapSort import Heap_sort
from MergeSort import Merge_sort

def Bubble_sort(lists):
    '''
    Bubble sort(冒泡排序): 每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换；
        1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        3.针对所有的元素重复以上的步骤，除了最后一个。
        4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    性能：
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：稳定
    :param lists:
    :return:
    '''
    for i in range(0, len(lists)):
        for j in range(i+1, len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]

    return lists

def Quick_sort(lists, left, right):
    '''
    Quick sort(快速排序):
        1）选择一个基准元素,通常选择第一个元素或者最后一个元素;
        2）通过一趟排序讲待排序的记录分割成独立的两部分，其中一部分记录的元素值均比基准元素值小,另一部分记录的元素值比基准值大;
        3）此时基准元素在其排好序后的正确位置;
        4）然后分别对这两部分记录用同样的方法继续进行排序，直到整个序列有序。
    性能：
        时间复杂度：O(nlog₂n)
        空间复杂度：O(nlog₂n)
        稳定性：不稳定
    :param lists:
    :param left:
    :param right:
    :return:
    '''
    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and key <= lists[right]:
            right -= 1
        lists[left] = lists[right]
        while left < right and key >= lists[left]:
            left += 1
        lists[right] = lists[left]
    lists[left] = key
    Quick_sort(lists, low, left-1)
    Quick_sort(lists, left+1, high)

    return lists

def Insert_sort(lists):
    '''
    Straight insert sort(插入排序): 先将序列的第1个记录看成是一个有序的子序列，然后从第2个记录逐个进行插入，直至整个序列有序为止。
        1.从第一个元素开始，该元素可以认为已经被排序
        2.取出下一个元素，在已经排序的元素序列中从后向前扫描
        3.如果该元素（已排序）大于新元素，将该元素移到下一位置
        4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
        5.将新元素插入到该位置后
        6.重复步骤2~5
    性能：
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：稳定
    :param lists:
    :return:
    '''
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
                print lists
            j -= 1

    return lists

def Shell_sort(lists, step):
    '''
    Shell sort(希尔排序): 先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
        待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
        （每次以一定步长(就是跳过等距的数)进行排序，直至步长为1）
    性能：
        时间复杂度：O(n)
        空间复杂度：O(n√n)
        稳定性：不稳定
    :param lists:
    :param step:
    :return:
    '''
    length = len(lists)
    group = length / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < length:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step

    return lists

def Simple_sort(lists):
    '''
    Simple selection sort(选择排序): 在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；
            然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换;
            依次类推，直到第n-1个元素（倒数第二个数）和第n个元素（最后一个数）比较为止。
        1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        3.重复第二步，直到所有元素均排序完毕。
    性能：
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：不稳定
    :param lists:
    :return:
    '''
    for i in range(len(lists)):
        x = i # index min label
        for j in range(i+1, len(lists)):
            if lists[j] < lists[x]:
                x = j
        lists[i], lists[x] = lists[x], lists[i]

    return lists

def Bucket_sort(lists):
    '''
    Bucket_sort(桶排序):设置一个个的桶，将需要排序的对象列表按顺序放入桶里面.
            (可以应用在排列考试成绩等等的场景里面)
    性能：
        时间复杂度：O(2n)
    :param lists:
    :return:
    '''
    buckets = [0] * (max(lists) - min(lists) + 1)
    for i in range(0, len(lists)):
        buckets[lists[i]-min(lists)] += 1

    re_list = []
    for i in range(0, len(buckets)):
        if buckets[i] != 0:
            re_list += [i+min(lists)]*buckets[i]

    return re_list

def Radix_sort(lists, radix=10):
    '''
    Problem
    Radix sort(基数排序):
        时间复杂度：O(d(r+n))
        空间复杂度：O(rd+n)
        稳定性：稳定
    :param lists:
    :param radix:
    :return:
    '''
    k = int(math.ceil(math.log(max(lists), radix)))
    print k
    bucket = [[] for i in range(radix)]
    print bucket
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]

    return lists

def Counter_sort(lists):
    '''
    Counter sort(计数排序):
        1.找出待排序的数组中最大和最小的元素
        2.统计数组中每个值为i的元素出现的次数，存入数组 C 的第 i 项
        3.对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
        4.反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
    :param lists:
    :return:
    '''
    min = 2147483647
    max = 0
    for x in lists:
        if x < min:
            min = x
        if x > max:
            max = x

    counter = [0] * (max-min+1)
    for index in lists:
        counter[index - min] += 1

    index = 0
    for i in range(max-min+1):
        for j in range(counter[i]):
            lists[index] = i + min
            index += 1

    return lists

if __name__ == '__main__':
    SortList = []
    #TestList = [3, 6, 5, 9, 7, 1, 8, 2, 4]
    TestList = [2, 5, 8, 9, 2]
    # Sortlists = Bubble_sort(Testlists)
    # Sortlists = Quick_sort(Testlists, 0, len(Testlists)-1)
    # SortList = Insert_sort(TestList)
    # SortList = Shell_sort(TestList, 2)
    # SortList = Simple_sort(TestList)
    # SortList = Heap_sort(TestList)
    # SortList = Merge_sort(TestList)
    # SortList = Bucket_sort(TestList)
    # SortList = Radix_sort(TestList)
    SortList = Counter_sort(TestList)
    print "The sort of lists is : ", SortList