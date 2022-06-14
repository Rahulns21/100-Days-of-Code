# Your program should print each number from 1 to 100 in turn
# When the number is divisible by 3 the instead of printing the number it should print 'Fizz'
# When the number is divisible by 5 the instead of printing the number it should print 'Buzz'
# And if the number is divisible by both 3 & 5 then it should print 'FizzBuzz'

# Write code below

for numbers in range(1, 101):
    if (numbers % 3) == 0 and (numbers % 5) == 0:
        print('Fizzbuzz')
    elif (numbers % 3) == 0:
        print('Fizz')
    elif (numbers % 5) == 0:
        print('Buzz')
    else:
        print(numbers)