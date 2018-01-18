# -*- coding: utf-8 -*-
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1

        if len(needle) == 0:
            return 0

        i = 0
        while i < len(haystack):
            if len(haystack) - i < len(needle):
                return -1

            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if haystack[i+j] == needle[j]:
                        j += 1
                    else:
                        break

                if j == len(needle):
                    return i

            i += 1

        return -1

if __name__ == '__main__':
    print Solution().strStr('aaaaa', 'ab')