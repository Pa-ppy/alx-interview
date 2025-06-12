#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given total amount.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list for storing the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
