# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 字符大小写排序（双指针/快排思想）
"""
class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        chars = list(chars)
        left = 0
        right = len(chars)-1

        while left < right:
            while left < right and chars[right] >= 'A' and chars[right] <= 'Z':
                right -= 1
            while left < right and chars[left] >= 'a' and chars[left] <= 'z':
                left += 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)

if __name__ == '__main__':
    # ch = 'DERLKAJKFKLAJFKAKLFJKLJFa'
    ch = 'abAcD'
    print Solution().sortLetters(chars=ch)