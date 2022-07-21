import os
from calculator_art import logo

#Function to clear terminal
def clear():
    os.system('cls')

#Calculator

print(logo)

#Add
def add(n1, n2):
    return n1+n2

#Subtract
def sub(n1, n2):
    return n1-n2

#Multiplication
def multiply(n1, n2):
    return n1*n2

#Division
def divide(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input('Enter the first number: '))
    for operators in operations:
        print(operators)

    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('Enter the second number: '))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {result}')

        if input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to exit: ') == 'y':
            num1 = result
        else:
            should_continue = False
            clear()
            calculator()

calculator()