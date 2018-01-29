# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 数值的整数次方，不考虑大数问题
"""
def PowerOfInt(base, exponent):
     """
     效率更高:
        当n为偶数, a^n = a^(n/2) * a^(n/2)
        当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
     :param base:
     :param exponent:
     :return:
     """
     if base == 0:
         return 0
     elif exponent == 0:
         return 1
     elif exponent == 1:
         return base
     elif exponent < 0:
         return 1.0 / PowerOfInt(base, -1 * exponent)
     else:
         tmp = PowerOfInt(base, exponent // 2)
         # 右移代替除以2
         if exponent % 2 == 0:
             return tmp * tmp
         else:
             return tmp * tmp * base

def PowerOfInt2(base, exponent):
    """
    Slower
    :param base:
    :param exponent:
    :return:
    """
    if base == 0:
        return 0
    if exponent == 0:
        return 1

    exp = abs(exponent)
    power = 1
    for i in range(exp):
        power *= base

    if exponent < 0:
        return 1.0 / power
    return power

if __name__ == '__main__':
    print PowerOfInt(4, 2)
    print PowerOfInt2(4, -1)