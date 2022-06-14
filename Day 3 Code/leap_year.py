# Code to find leap year

enter_year = int(input('Enter any year: '))

divisible_by_4 = enter_year % 4
divisible_by_100 = enter_year % 100
divisible_by_400 = enter_year % 400

if divisible_by_4 == 0:
    if divisible_by_100 == 0:
        if divisible_by_400 == 0:
            print(f'{enter_year} is a leap year')
        else:
            print(f'{enter_year} is not a leap year')
    else:
        print(f'{enter_year} is a leap year')
else: 
    print(f'{enter_year} is not a leap year')