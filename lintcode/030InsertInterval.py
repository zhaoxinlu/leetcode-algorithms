# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 插入区间
"""
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        # write your code here
        results = []
        insertPos = 0

        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)

        return results

if __name__ == '__main__':
    i1 = Interval(1, 2)
    i2 = Interval(5, 9)
    intervals = [i1, i2]
    newInt = Interval(2, 6)
    r = Solution().insert(intervals, newInt)
    for i in r:
        print i.start, i.end