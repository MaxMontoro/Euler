'''
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import unittest


'''
1.
Naive solution involving actually writing out the all numbers with letters and then counting the lenght of the entire string.
'''

numbers = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
           10:'ten', 11: 'eleven', 12: 'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 
           16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 
           40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred', 
           1000:'one thousand'}

numbers_with_words = []

def number_with_words(num):
    if num in numbers:
        number_with_words = numbers[num]
    elif 20<num<100:
        tens, ones = [int(d) for d in str(num)]
        tens = numbers[tens*10]
        number_with_words = tens + '-' + numbers[ones]
    elif 100<num:
        hundreds, tens, ones = [int(i) for i in str(num)]
        hundreds = numbers[hundreds] + ' ' + 'hundred'
        if str(num)[1:] == '00':
            number_with_words = hundreds
        elif tens == 0:
            tens = ' and '
            ones = numbers[ones]
            number_with_words = hundreds + tens + ones
        elif int(str(num)[1:]) in numbers:
            tens = numbers[int(str(num)[1:])]
            number_with_words = hundreds + ' and ' + tens
        else:
            tens = numbers[tens*10]
            ones = numbers[ones]
            number_with_words = hundreds + ' and ' + tens + '-' + ones
    return number_with_words

def get_length(number_with_words):
    number_with_words = number_with_words.strip().replace('-', '').replace(' ', '')
    return len(number_with_words)

sum_of_letters = 0
for num in range(1,1001):
    number_w_words = number_with_words(num)
    sum_of_letters += get_length(number_w_words)
print(sum_of_letters)    

class TestNumbers(unittest.TestCase):

    def test_342(self):
        self.assertEqual(number_with_words(342), 'three hundred and forty-two')
        
    def test_115(self):
        self.assertEqual(number_with_words(115), 'one hundred and fifteen')
        
    def test_length_342(self):
        self.assertEqual(get_length(number_with_words(342)), 23)
        
    def test_length_115(self):
        self.assertEqual(get_length(number_with_words(115)), 20)

if __name__ == '__main__':
    unittest.main()