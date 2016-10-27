'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def squares(n):
    '''Yield squares of numbers from 1 to n'''
    for number in range(n):
        yield number**2
    
    
def sums(n):
    '''Yield the sum of numbers from 1 to n'''
    summa = 0
    for number in range(n):
        summa += number
        yield summa
        
def sum_of_squares(n):
    '''Yield sum of squares of numbers from 1 to n'''
    summa = 0
    for number in squares(n):
        summa += number
        yield summa
        
def square_of_sum(n):
    '''Yield square of sum of numbers'''
    square = 1
    for number in sums(n):
        square = number ** 2
        yield square
        
def diff_of_sumsquare_and_squaresum(n):
    '''Yield difference'''
    for number in square_of_sum(n):
        for number2 in sum_of_squares(n):
            diff = number - number2
    yield diff
            