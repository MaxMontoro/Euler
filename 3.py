'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(n):
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor: # if remainder is not null
            divisor += 1
        else: # remainder is null -> n can be divieded by divisor
            n //= divisor
    return n

print(largest_prime_factor(600851475143))