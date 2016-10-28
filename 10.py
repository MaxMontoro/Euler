'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from itertools import count
from math import sqrt
            
def prime_generator_under(n):
    yield 2
    for num in count(3):
        prime = True
        for divisor in range(int(sqrt(num)), 1,-1):
            if num % divisor == 0:
                prime = False
                break
        if prime:
            if num < n:
                yield num
            else:
                return
            
summa = 0
first_100_primes = []
for i in nth_prime_generator(100):
    first_100_primes.append(i)
    summa += i
    
# print(first_100_primes)

def sum_of_primes_below(n):
    summa = 0
    for prime in prime_generator_under(n):
        summa += prime
    yield summa

counti = 0
summa = 0
for i in prime_generator_under(2000000):
    counti += 1
    summa += i
print(counti)
print("sum: ", summa)
    
for i in sum_of_primes_below(100):
    print(i)
    
