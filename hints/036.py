"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def strip_0b_from_binary(binary):
    return binary[2:]


def is_double_base_palindrome(n):
    if not is_palindrome(n):
        return False
    binary = bin(n)
    if not is_palindrome(strip_0b_from_binary(binary)):
        return False
    return True
    
    
def sum_of_double_palindromes_below(n):
    summa = 0
    for number in range(n):
        if is_double_base_palindrome(number):
            summa += number
    return summa
    

print(sum_of_double_palindromes_below(1000000))