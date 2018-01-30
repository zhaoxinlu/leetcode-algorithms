# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-30
Function: 包含min函数的栈实现
"""
class minStack(object):
    """
    借助两个辅助列表（一个存放元素，一个存放每次的最小元素）及成员变量（最小元素）
    """
    def __init__(self):
        self.mS_data = []
        self.mS_min = []
        self.mS = None

    def min(self):
        return self.mS

    def push(self, value):
        self.mS_data.append(value)

        if self.mS == None:
            self.mS = value
        else:
            if self.mS > value:
                self.mS = value

        self.mS_min.append(self.mS)

    def pop(self):
        if len(self.mS_data) == 0:
            return False
        elif len(self.mS_data) == 1:
            self.mS_min.pop()
            self.mS = None
            return self.mS_data.pop()
        else:
            self.mS_min.pop()
            self.mS = self.mS_min[-1]
            return self.mS_data.pop()

if __name__ == '__main__':
    ms = minStack()
    ms.push(3)
    ms.push(4)
    ms.push(2)
    ms.push(1)
    print ms.min()

    ms.pop()
    print ms.min()

    ms.pop()
    print ms.min()

    ms.pop()
    print ms.min()

    ms.pop()
    print ms.min()