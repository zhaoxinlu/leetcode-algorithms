# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-13
Function: 连续子数组的最大和
"""
def maxSumOfConSubArray(arr):
    """
    1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
        ①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
        ②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
    2、判断累加值是否大于最大值：如果大于最大值，则最大和更新；否则，继续保留之前的最大和
    :param arr:
    :return: max SUM
    """
    if arr == None or len(arr) <= 0:
        return False

    curSum = 0
    maxSum = arr[0]

    for i in range(0, len(arr)):
        if curSum <= 0:
            curSum = arr[i]
        else:
            curSum += arr[i]

        if curSum > maxSum:
            maxSum = curSum

    return maxSum

def maxSumOfConSubArray_dp(arr):
    """
    动态规划实现，dp[i]表示以第i个数字结尾的子数组的最大和
    :param arr:
    :return:
    """
    dp = [0] * (len(arr))

    for i in range(0, len(arr)):
        if i == 0 or dp[i-1] <= 0:
            dp[i] = arr[i]
        else:
            dp[i] = dp[i-1] + arr[i]

    return max(dp)

if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print maxSumOfConSubArray(arr)
    print maxSumOfConSubArray_dp(arr)