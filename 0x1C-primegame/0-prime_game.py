#!/usr/bin/python3
"""
Find the winner of the game involving prime numbers.
Notes: count the prime numbers only, it's faster than checking all numbers.
"""


def nextPrime(n, limit):
    """ Hardcore function that returns the next prime number after n. """
    if n == 2:
        return 3
    oldPrime = n
    while True:
        n += 2 # skip even numbers
        if limit < n:
            return -1
        flag = 0
        for factor in range(3, oldPrime + 1, 2): # check all odd factors
            if n % factor == 0:
                flag += 1
                break
        if flag == 0:
            return n

def roundWinner(num):
    """ Return the winner of the round. """
    playerSwitch = -1 # 1: playerOne, -1: playerTwo
    prime = 2
    while prime != -1:
        playerSwitch *= -1
        prime = nextPrime(prime, num)
    if playerSwitch == 1:
        return 1
    else:
        return 2

def isWinner(x, nums):
    totalRounds = min(x, len(nums))
    if totalRounds == 0:
        return None
    pOneName = "Maria"
    pTwoName = "Ben"
    playerOne = playerTwo = 0 # the number of rounds won by each player
    for i in range(totalRounds):
        winner = roundWinner(nums[i])
        if winner == 1:
            playerOne += 1
        elif winner == 2:
            playerTwo += 1
    if playerOne > playerTwo:
        return pOneName
    elif playerOne < playerTwo:
        return pTwoName
    else:
        return None
