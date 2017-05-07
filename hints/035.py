"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from collections import deque


def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True


def my_rotate(nums, shift):
    q = deque(nums)
    q.rotate(shift)
    return list(q)

cache = {}

def is_circular_prime(n):
    if not is_prime(n):
        return False
    digits = deque(list(str(n)))
    for number in (my_rotate(digits, shift) for shift in range(len(digits))):
        if not is_prime(int(''.join(number))):
            return False
    return True


def circular_primes_below_n(n):
    circ_primes = 0
    for number in range(2, n):
        if is_circular_prime(number):
            circ_primes += 1
    return circ_primes

n = 1000000

