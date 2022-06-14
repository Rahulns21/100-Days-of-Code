# Conditional Operators
# > : Greater Than
# < : Lesser Than
# >= : Greater than or Equal to
# <= : Lesser than or Equal to
# == : Equal to
# != : Not Equal to

print('Welcome to the Roller Coaster')
height = int(input('What is your height in cm? '))
age = int(input('What is your age? '))
bill = 0

if height >= 120:
    print('User can ride')
    if age <= 12:
        bill = 5
        print('User must pay $5')
    elif age <= 18:
        bill = 7
        print('User must pay $7')
    else:
        bill = 12
        print('User must pay $12')

    wants_photo = input('Do you want a picture? Y or N: ')
    if wants_photo == 'Y':
        bill += 3
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')
else:
    print('User cannot ride')
    

