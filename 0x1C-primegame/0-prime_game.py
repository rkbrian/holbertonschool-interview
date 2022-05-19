#!/usr/bin/python3
"""
Find the winner of the game involving prime numbers.
Notes: count the prime numbers only, it's faster than checking all numbers.
"""


def closestPrime(n):
    """ Return the closest prime number next to n. """
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
    """ Hardcore function that returns the next prime number after n. """
    if n == 2:
        return 3
    while True:
        n += 2  # skip even numbers
        flag = 0
        """ check odd factors, sq root of n locks commutative property. """
        for factor in range(3, int(n ** 0.5) + 1, 2):
            if n % factor == 0:
                flag += 1
                break
        if flag == 0:
            return n


def roundWinner(num, prime, lastWinner):
    """ Return the winner of the round. """
    if prime > num:
        return lastWinner
    playerSwitch = lastWinner  # 1: playerOne, -1: playerTwo
    while prime <= num:
        playerSwitch *= -1
        prime = nextPrime(prime)
    if playerSwitch == 1:
        return 1
    else:
        return -1


def isWinner(x, nums):
    """ Return the name of the winner. """
    totalRounds = min(x, len(nums))
    if totalRounds <= 0:
        return None
    nums = sorted(nums)  # played range won't repeat
    pOneName = "Maria"
    pTwoName = "Ben"
    playerOne = playerTwo = 0  # the number of rounds won by each player
    lastWinner = -1
    for i in range(totalRounds):
        prime = closestPrime(nums[i])
        winner = roundWinner(nums[i], prime, lastWinner)
        if winner > 0:
            playerOne += 1
            lastWinner = 1
        elif winner < 0:
            playerTwo += 1
            lastWinner = -1
    if playerOne > playerTwo:
        return pOneName
    elif playerOne < playerTwo:
        return pTwoName
    else:  # somehow the draw case is considered playerOne wins
        return pOneName
