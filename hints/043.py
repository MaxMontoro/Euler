"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

def generate_all_pandigital_numbers(length):
    for num in permutations(list(range(length))[::-1]):
        yield int(''.join(str(d) for d in num))

def is_divisible_by_x(num, x):
    return num % x == 0

primes = (2,3,5,7,11,13,17)

summa = 0

for pandigital in generate_all_pandigital_numbers(length=10):
    subnumbers = [int(str(pandigital)[i:i+3]) for i in range(1, len(str(pandigital))-2)]
    pairs = zip(subnumbers, primes)
    if all(is_divisible_by_x(pair[0], pair[1]) for pair in pairs) and len(set(str(pandigital))) == 10:
        print(pandigital    )
        summa += pandigital

print(summa)
