'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def brute_force():
    largest = 0
    for multiplier_one in range(1000):
        for multiplier_two in range(1000):
            product = (multiplier_one*multiplier_two)
            if str(product)[::-1] == str(product):
                if product > largest:
                    largest = product
    return largest
        

print(brute_force())