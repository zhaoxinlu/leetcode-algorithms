# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 翻转单词
    单词的构成：无空格字母构成一个单词
    输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
    如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
"""
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        """
        s = s.strip()
        if len(s) == 0:
            return ""
        split_items = s.split(" ")
        ans = [x for x in split_items if len(x) > 0]
        return ''.join(ans[::-1])

        :param s:
        :return:
        """
        if s == '':
            return ''
        s = list(s.strip())
        self.reverse(s, 0, len(s)-1)
        s.append('\0')

        pStart = 0
        pEnd = 0

        while pStart < len(s) and pEnd < len(s):
            if s[pStart] == ' ':
                pStart += 1
                pEnd += 1
            elif (s[pEnd] == ' ' and s[pEnd+1] != ' ') or s[pEnd] == '\0':
                self.reverse(s, pStart, pEnd-1)
                pStart = pEnd + 1
                pEnd += 1
            elif s[pEnd] == ' ' and s[pEnd+1] == ' ':
                s.pop(pEnd+1)
            else:
                pEnd += 1

        s.pop()
        return ''.join(s)

    def reverse(self, s, start, end):
        # s = list(s)
        i, j = start, end

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        # s = ''.join(s)
        return s

if __name__ == '__main__':
    str = 'word'
    print Solution().reverseWords(str)
    # print Solution().reverse('abc d', 0, 4)