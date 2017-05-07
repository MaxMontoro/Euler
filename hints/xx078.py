'''
Coin partitions
Problem 78
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

from itertools import count

cache = {}
n = 1000
integers = tuple(range(n,1))
def exp_sum(n, integers=tuple(range(n,1,-1))):
    if (n, integers) in cache:
        print('returning from cache')
        return cache[(n, integers)]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    if n > 0 and len(integers) == 0:
        return 0
    else:    
        largest, rest = integers[0], integers[1:] 
    cache[(n-largest, integers)] = exp_sum(n-largest, integers)
    cache[(n, rest)] = exp_sum(n, rest)
    return cache[(n-largest, integers)] + cache[(n, rest)]


for n in count(10):
    coins = tuple(range(n-1,1, -1))
    try:
        result =  exp_sum(n, coins)
        if result % 1000000 == 0:
            print(result)
            print(n)
            break
    except RecursionError:
        print(result)
