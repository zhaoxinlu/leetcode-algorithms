# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-13
Function: 1～n整数中1出现的次数
"""
def numOf1Between1AndN(n):
    """
    计数，累计1在1～n的总次数，时间效率较低
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n < 0:
        return None

    count = 0

    for i in range(1, n+1):
        count += numOf1(i)

    return count

def numOf1(num):
    """
    每个整数含有1的个数
    :param num:
    :return:
    """
    times = 0
    while num:
        if num % 10 == 1:
            times += 1
        num /= 10

    return times

##########################################
"""
剑指Offer新思路
"""
##########################################
def get_digits(n):
    """
    获取一整数的位数，23456为5位的整数
    :param n:
    :return:
    """
    ret = 0

    while n:
        ret += 1
        n /= 10

    return ret

def getNumOf1EachDigit(digit):
    """
    1位数，1-9中，1一共出现了1次；
    2位数，10-99中，10-19的十位上一共出现了10*1=10次，对于每个十位开头的数字10-19、20-29，每个数个位上出现的是1-9中1出现的次数，共有9个区间9*1=9次；
    3位数，100-999，100-199百位上出现了10**2=100次，对于每个百位数开头，例如100-199，200-299，低位上其实就是0-99这个区间上1出现的次数，一共9个区间 9*19=171次；
    由此推测，对于1-9，10-99，100-999，每个n位数中包含1的个数公式为：
      f(1) = 1
      f(2) = 9 * f(1) + 10 ** 1
      f(3) = 9 * f(2) + 10 ** 2
      f(n) = 9 * f(n-1) + 10 ** (n-1)
    :param digit:
    :return:
    """
    if digit <= 0:
        return 0
    if digit == 1:
        return 1

    number = 9 * getNumOf1EachDigit(digit-1) + 10 ** (digit-1)

    return number + getNumOf1EachDigit(digit-1)

def numOf1Between1AndN_2(n):
    """
    时间效率很高
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    if n >= 1 and n < 10:
        return 1

    digit = get_digits(n)
    low_nums = getNumOf1EachDigit(digit-1)
    high = int(str(n)[0])
    low = n - high * 10 ** (digit-1)

    if high == 1:
        high_nums = low + 1
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit-1)
        all_nums = high_nums + low_nums * (high - 1)

    return low_nums + all_nums + numOf1Between1AndN_2(low)

if __name__ == '__main__':
    # print numOf1Between1AndN(9923446)
    # print get_digits(23456)
    # print getNumOf1EachDigit(5)
    print numOf1Between1AndN_2(9923446)