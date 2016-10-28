'''
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def brute_force():
    for a in range(1,999):
        for b in range(1,999):
            for c in range(1,999):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a, b, c
                    
def tidier():
    for c in range(2,999):
        for a in range(1, c):
            b = 1000 - c - a
            if a**2 + b**2 == c**2:
                return a, b, c
                    
#print(find_special_Pythagorean())
print(tidier())