
def print_primes(lower, limit):
    for number in range(lower, limit + 1):
        if is_prime(number):
            print(number)


def is_prime(number):
    if number <= 1:
        return False
    for possible_divisor in range(2, int(number**(1 / 2)) + 1):
        if number % possible_divisor == 0:
            return False
    return True
