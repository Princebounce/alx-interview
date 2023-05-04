#!/usr/bin/python3
import math
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste
    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
def minOperations(n):
    if n == 1:
        return 0
    if is_prime(n):
        return 0
    dp = [math.inf] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        for d in range(2, i):
            if i % d == 0:
                dp[i] = min(dp[i], dp[d] + (i//d))
    return dp[n]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

