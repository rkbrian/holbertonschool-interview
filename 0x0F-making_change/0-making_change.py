#!/usr/bin/python3
"""Techique used: binary search"""


def makeMatch(coins, total, count):
    """Recursively search for the fewest number of coins needed to make change"""
    if len(coins) == 1 and total % coins[0] == 0:
        """If there is only one coin and the total is divisible by it"""
        return int(total / coins[0] + count)
    elif len(coins) == 1:
        """If there is only one coin and the total is not divisible by it, failed"""
        return -1
    if coins[0] > total:
        """If the first coin is not appropriate"""
        return makeMatch(coins[1:], total, count)
    curr = makeMatch(coins, total - coins[0], count + 1)
    next = makeMatch(coins[1:], total, count)
    if curr > 0 and next > 0:
        """If both options are valid"""
        return min(curr, next)
    elif curr > 0:
        return curr
    elif next > 0:
        return next
    return -1

def makeChange(coins, total):
    """Big O: O(logn)"""
    if total < 0 or len(coins) == 0:
        return -1
    if total == 0:
        return 0
    if min(coins) > total:
        return -1
    return makeMatch(coins, total, 0)
