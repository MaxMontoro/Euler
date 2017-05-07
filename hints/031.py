'''
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

initial_coins = [200,100,50,20,10,5,2,1]
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
    
print(change(200, initial_coins))