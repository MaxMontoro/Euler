'''
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
from timeit import Timer

setup = '''
def brute_force_with_for_loop(n):
    summa = 0
    for i in range(n):
       if i % 3 == 0 or i % 5 == 0:
          summa += i


def list_comprehension(n):
    summa = sum((i for i in range(n) if i % 3 == 0 or i % 5 == 0))
    
def generator_function(n):
    summa = 0
    for i in range(n):
       if i % 3 == 0 or i % 5 == 0:
          summa += i
          yield summa
    print(summa)

n = 1000
'''

def generator_function(n):
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            yield i
        i += 1

def list_comprehension(n):
    summa = sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])
    return summa
    
print(sum(generator_function(1000)))
print(list_comprehension(1000))


t = Timer("brute_force_with_for_loop(n)", setup=setup)
t_list_compr = Timer("list_comprehension(n)", setup=setup)
t_gen = Timer("generator_function(n)", setup=setup)


print("Brute force time:       ", t.timeit(number=10000))
print("List comprehension time:", t_list_compr.timeit(number=10000))
print("Generator function     :", t_gen.timeit(number=10000))
    
