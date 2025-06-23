#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """Check if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n):
    """Count number of primes up to n (inclusive)"""
    sieve = [True for _ in range(n + 1)]
    sieve[0:2] = [False, False]
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return count


def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = count_primes(nums[i])
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
