'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def len_collatz_memo(start, terms=1, memo={1:1}):
    if start in memo:
        return memo[start]
    if start == 1:
        return terms
    if start % 2 == 0:
        terms = len_collatz_memo(start//2)+1
    else:
        terms = len_collatz_memo(3*start + 1) + 1
    memo[start] = terms
    return terms

longest = 0
started_at = 0
for start in range(1,1000000):
    length = len_collatz_memo(start)
    if length > longest:
        longest = length
        started_at = start
        print(started_at, longest)
    
print(started_at, longest)