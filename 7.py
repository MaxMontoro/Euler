'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from itertools import count, takewhile

def prime_generator(n):
    index = 1
    for num in count(3):
        prime = True
        for divisor in range((num//2)+1, 1,-1):
            if num % divisor == 0:
                prime = False
                break
        if prime:
            index += 1
            if index == n:
                return num