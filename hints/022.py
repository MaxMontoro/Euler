'''
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string
'''
with open('p022_names.txt', 'r') as data:
    names = sorted([name.strip('"') for name in data.read().split(',')])
    alphabet = string.ascii_uppercase
    summa = 0
    for name in names:
        position = names.index(name) + 1
        value = sum([alphabet.index(letter)+1 for letter in name])
        score = position * value
        summa += score
        if name == 'COLIN': # testing for COLIN
            print(position)
            print(value)
            print(score)
    print(summa)
    
'''

# Two list comprehensions perhaps make it more 'Pythonic' but much less readable:
    
    
with open('p022_names.txt', 'r') as data:  
    names = sorted([name.strip('"') for name in data.read().split(',')])
    print(sum([(names.index(name) + 1) * sum([string.ascii_uppercase.index(letter)+1 for letter in name]) for name in names]))