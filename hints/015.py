'''
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

'''
I really struggled with this, so I looked for hints on the internet. The solution was handed to me by:
http://www.robertdickau.com/manhattan.html.

At least I learned about Pascal's triangle and the central binomial coefficients.

https://en.wikipedia.org/wiki/Binomial_coefficient
'''
n = 40
k = 20

n_fact = 1 
for i in range(1,n+1):
    n_fact *= i
k_fact = 1

for i in range(1,k+1):
    k_fact *= i
    
k_n_fact = 1
for i in range(1,n-k+1):
    k_n_fact *= i
    
solution = n_fact/(k_fact*(k_n_fact))
print(solution)