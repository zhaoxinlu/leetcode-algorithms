# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：简化路径--利用栈
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        result = ''

        while i < len(path):
            j = i+1
            while j < len(path) and path[j] != '/':
                j += 1

            tmp = path[i+1:j]
            if len(tmp) > 0:
                if tmp == '..':
                    if stack != []:
                        stack.pop()
                elif tmp != '.':
                    stack.append(tmp)

            i = j

        if stack == []:
            result += '/'
        else:
            for i in range(len(stack)):
                result += ('/'+stack[i])

        return result

if __name__ == '__main__':
    path = '/a/./b/../../c/'
    print Solution().simplifyPath(path)