#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([1, 2, 5, 10, 25, 50, 100], 972))

print(makeChange([1, 4, 5, 10], 1278652))