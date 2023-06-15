#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet the given amount total.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total
    # Initialize all values with infinity except the 0th index, which is set to 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate over all possible totals from 1 to the given total
    for i in range(1, total + 1):
        # Iterate over all available coin denominations
        for coin in coins:
            if coin <= i:
                # Calculate the minimum number of coins needed for the current total
                # by considering the previous total and subtracting the coin value
                num_coins = min_coins[i - coin] + 1
                # Update the minimum number of coins if the current number is smaller
                min_coins[i] = min(min_coins[i], num_coins)

    # If the minimum number of coins for the total is still infinity, it means
    # the total cannot be met by any combination of coins, so return -1
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]

