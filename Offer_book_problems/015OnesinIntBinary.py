# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 整数二进制中1的个数
"""
def NumOfOneInBinary(num):
    num = int(num)

    count = 0
    while num != 0:
        ret = num % 2
        if ret == 1:
            count += 1

        num = num / 2

    return count

if __name__ == '__main__':
    print NumOfOneInBinary(2)