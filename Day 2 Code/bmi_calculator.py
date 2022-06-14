# Bmi Calculator
# Bmi = weight(kg)/height^2(m^2)

height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')

bmi = int(weight) / float(height) ** 2
print(bmi)

if (float(bmi <= 18)):
    print('You are underweight')

if (float(bmi >= 25)):
    print('You are overweight')

if (float(bmi <= 18) and float(bmi >= 25)):
    print('You are normal size')