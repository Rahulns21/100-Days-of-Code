#Check number is Odd or Even

number = int(input('Enter any number: '))
result = number % 2
if result == 0:
    print('This is even number')
else:
    print('This is odd number')