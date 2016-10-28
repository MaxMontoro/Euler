'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from itertools import count
from math import sqrt
from timeit import Timer

            
def prime_generator_below(n):
    yield 2
    for num in count(3,2):
        prime = True
        for divisor in range(int(sqrt(num)), 2,-1):
            if num % divisor == 0:
                prime = False
                break
        if prime:
            if num < n:
                yield num
            else:
                return

def sum_of_primes_below(n):
    summa = 0
    for prime in prime_generator_below(n):
        summa += prime
    yield summa

for i in sum_of_primes_below(2000000):
    print(i)
    
