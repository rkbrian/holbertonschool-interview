#!/usr/bin/python3
"""
Find the winner of the game involving prime numbers.
Notes: count the prime numbers only, it's faster than checking all numbers.
"""


def closestPrime(n):
    """
    Return the closest prime number after regular number n,
    or return n if it is a prime number. Prime finding technique involves
    division by odd factors, and sq root of n locks commutative property.
    """
    if n <= 2:
        return 2
    elif n % 2 == 0:
        n += 1
    while True:
        flag = 0
        for factor in range(3, int(n ** 0.5) + 1, 2):
            if n % factor == 0:
                flag += 1
                break
        if flag == 0:
            return n
        n += 2  # skip even numbers


def nextPrime(n):
    """ Return the next prime number after the prime number n. """
    if n == 2:
        return 3
    while True:
        n += 2  # skip even numbers
        flag = 0
        for factor in range(3, int(n ** 0.5) + 1, 2):
            if n % factor == 0:
                flag += 1
                break
        if flag == 0:
            return n


def roundWinner(num, prime, winner):
    """
    Return the winner of the round.
    Determined by the starting prime number, the section limit,
    and the winner switcher: 1 for playerOne, -1 for playerTwo.
    """
    if prime > num:
        return winner
    while prime <= num:
        winner *= -1
        prime = nextPrime(prime)
    return winner


def isWinner(x, nums):
    """
    Return the name of the winner.
    Optimized by removing the iterated ranges and jump to the last result,
    requiring the array to be sorted.
    """
    totalRounds = min(x, len(nums))
    if totalRounds <= 0:
        return None
    nums = sorted(nums)  # played range won't repeat
    pOneName = "Maria"
    pTwoName = "Ben"
    playerOne = playerTwo = 0  # the number of rounds won by each player
    winner = -1  # 1: playerOne, -1: playerTwo
    for i in range(totalRounds):
        if i == 0:
            prime = 2
        else:
            prime = closestPrime(nums[i])
        winner = roundWinner(nums[i], prime, winner)
        if winner > 0:
            playerOne += 1
        elif winner < 0:
            playerTwo += 1
    if playerOne > playerTwo:
        return pOneName
    elif playerOne < playerTwo:
        return pTwoName
    else:  # somehow the draw case is considered playerOne wins
        return pOneName
