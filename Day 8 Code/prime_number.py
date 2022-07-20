# Code to check prime number
n = int(input('Check this number: '))

def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print('Its is a prime number')
    else:
        print('Its not a prime number')

prime_checker(number=n)