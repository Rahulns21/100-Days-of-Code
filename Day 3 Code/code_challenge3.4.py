# Pizza Order Exercise

print('Welcome to Pizza Shop')
size = input('What size pizza do you want? S, M, or L: ')
add_pepperoni = input('Do you want pepperoni? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')
bill = 0

if size == 'S':
    bill = 15
    print('You must pay $15')
    if add_pepperoni == 'Y':
        bill += 2
        print('You must pay extra $2')
    
    if extra_cheese == 'Y':
        bill += 1
        print('You must pay extra $1')
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')

elif size == 'M':
    bill = 20
    print('You must pay $20')
    if add_pepperoni == 'Y':
        bill += 3
        print('You must pay extra $3')
    
    if extra_cheese == 'Y':
        bill += 1
        print('You must pay extra $1')
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')
elif size == 'L':
    bill = 25
    print('You must pay $25')
    if add_pepperoni == 'Y':
        bill += 3
        print('You must pay extra $3')
    
    if extra_cheese == 'Y':
        bill += 1
        print('You must pay extra $1')
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')
else:
    print('Size not available')
