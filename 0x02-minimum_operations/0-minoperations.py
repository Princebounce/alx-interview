#!/usr/bin/python3
""" Script that computes a minimum operations needed in a copyall - paste task
"""

def minOperations(n):

    """
    Method for compute the minimum number of operations for task Copy All and Paste
    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    
    return sum(factors)

