# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-21
算法思想： 最长连续序列--O(n)
"""
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        """
        vector里面的元素作为key，元素所在连续序列的长度作为value
        对于元素i，我们就需要找i+1，i-1，如果有将i的value更新为i+1 & i-1的value和并加一，相当于连接了这三个连续的数，
        同时还需要将这个连续数列的首位两端也更新.
        :param num:
        :return:
        """
        # write your code here
        if num == None or len(num) == 0:
            return 0

        numDict = {}
        maxLen = 0

        for i in num:
            if i not in numDict:
                l, r =0, 0
                if i-1 in numDict:
                    l = numDict[i-1]
                if i+1 in numDict:
                    r = numDict[i+1]

                numDict[i] = l+r+1
                numDict[i+r] = l+r+1
                numDict[i-l] = l+r+1

                maxLen = max(maxLen, numDict[i])

        return maxLen

if __name__ == '__main__':
    num = [100, 4, 200, 1, 3, 2]
    print Solution().longestConsecutive(num)