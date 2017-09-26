"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

initial_coins = list(range(99, 0,-1))
cache = {}

def change(amount, coins = initial_coins):
    '''Returns the number of possible ways that amount can be changed (in Hungarian coins)'''
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    if amount > 0 and len(coins) == 0:
        return 0
    else:
        if amount in cache:
            return cache[amount]
        biggest, rest = coins[0], coins[1:]
        return change(amount-biggest, coins) + change(amount, rest)
    
print(change(100, initial_coins))