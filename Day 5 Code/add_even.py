# Write a program to calculate sum of all even numbers from 1 to 100

sum = 0
for number in range(1, 101):
    if (number % 2) == 0:
        sum += number

print(f'The sum of all even numbers from 1 to 100: {sum}')