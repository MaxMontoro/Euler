"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def generate_all_pandigital_numbers(length):
    for num in permutations(list(range(length-1, 0, -1))):
        yield int(''.join(str(d) for d in num))

def find_largest_pandigital_prime():
    for n in range(10, 1, -1):
        for number in generate_all_pandigital_numbers(n):
            if is_prime(number):
                return number


print(find_largest_pandigital_prime())
