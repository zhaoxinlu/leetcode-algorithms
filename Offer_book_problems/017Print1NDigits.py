# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 打印从1到最大的n位数（大数问题）
    解决大数问题：用字符串或者数组来表达大数
"""
def PrintNDigits1(num):
    """
    未考虑大数问题，n很大时会超出int或者long long的范围
    :param num:
    :return:
    """
    if num <= 0:
        return False

    upper = 1
    for i in range(0, num):
        upper = upper * 10
    for i in range(1, upper):
        print i

def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return False

    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, n, 0)

def Print1ToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return

    for i in range(10):
        number[index+1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, length, index+1)

def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print '%c' % number[i]
    print ''

if __name__ == '__main__':
    # PrintNDigits1(1)
    print Print1ToMaxOfNDigits(2)