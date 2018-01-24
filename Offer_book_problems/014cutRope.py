# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 剪绳子
    给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)每段绳子的长度记为k[0],k[1],…,k[m].请问k[0]k[1]…*k[m]可能的最大乘积是多少？
    例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
"""
def cutRope_dp(length):
    """
    动态规划算法实现
    :param length:
    :return:
    """
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    dp = [0] * (length+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, length+1):
        max = 0
        for j in range(1, i/2 + 1):
            dps = dp[j] * dp[i-j]
            if max < dps:
                max = dps

        dp[i] = max

    return dp[length]

def cutRope_greedy(length):
    """
    贪心算法实现
    :param length:
    :return:
    """
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    # len>=5时
    timesOf3 = length / 3

    if length - timesOf3 * 3 == 1:
        timesOf3 -= 1

    timesOf2 = (length - timesOf3 * 3) / 2

    return pow(3, timesOf3) * pow(2, timesOf2)

if __name__ == '__main__':
    rope_length = 16
    print cutRope_dp(length=rope_length)
    print cutRope_greedy(length=rope_length)