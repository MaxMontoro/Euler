'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from timeit import Timer

def divisable(dividend, divisor):
    if dividend % divisor:
        return False
    return True

def brute_force():
    solution = 0
    candidate = 1
    divisors = range(1,11)
    while not solution:
        candidate += 1
        for divisor in divisors:
            if not divisable(candidate, divisor):
                break
            if divisor == divisors[-1]:
                solution = candidate
            continue
    return solution 


from itertools import count, takewhile


def smallest(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = 1
    for prime in primes:
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        result *= bprime
    return result

# from @ondra at StackOverflow

#print(brute_force())
print(smallest(20))



setup='''
from itertools import count, takewhile

def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result

def divisable(dividend, divisor):
    if dividend % divisor:
        return False
    return True

    
def brute_force():
    solution = 0
    candidate = 1
    divisors = range(1,11)
    while not solution:
        candidate += 1
        for divisor in divisors:
            if not divisable(candidate, divisor):
                break
            if divisor == divisors[-1]:
                solution = candidate
            continue
    return solution     
'''
t_1 = Timer("brute_force()", setup=setup)
t_2 = Timer("smallest(20)", setup=setup)
print(t_1.timeit(number=100))
print(t_2.timeit(number=100))