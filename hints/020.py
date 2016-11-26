'''
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

cache = {}
def fact(n):
    if n in [1,2]:
        return n
    if n in cache:
        return cache[n]
    cache[n] = n * fact(n-1)
    return cache[n]

def sum_digits(n):
    return sum([int(digit) for digit in str(n)])

