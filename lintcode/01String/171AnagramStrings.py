# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 乱序字符串--
    对传进来的数组中的所有元素，进行排序。
    因为我们按照特定的排序方式进行排序，必然会导致一样的排序结果。
    那么只要排序后的字符串是一致的，那么我们就可以肯定这几个字符串是相同的字符串.
"""
class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        if strs == None or len(strs) <= 1:
            return strs

        results = []
        strsDict = {}

        for i in range(len(strs)):
            s = self.strSort(strs[i])
            if s in strsDict:
                strsDict[s].append(i)
            else:
                strsDict[s] = [i]

        for j in strsDict.keys():
            if len(strsDict[j]) > 1:
                for k in strsDict[j]:
                    results.append(strs[k])

        return results

    def strSort(self, s):
        s = list(s)
        s.sort()
        return ''.join(s)

if __name__ == '__main__':
    # strs = ["lint", "intl", "inlt", "code"]
    strs = ["", ""]
    print Solution().anagrams(strs)