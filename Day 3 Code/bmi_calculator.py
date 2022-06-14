# Bmi Calculator

height = float(input('What is your height in m: '))
weight = float(input('What is your weight in kg: '))

bmi = float(round(weight / height ** 2, 2))

if bmi < 18.5:
    print(f'Your bmi is {bmi}, You are underweight')
elif bmi < 25:
    print(f'Your bmi is {bmi}, You have normal weight')
elif bmi < 30:
    print(f'Your bmi is {bmi}, You are overweight')
elif bmi < 35:
    print(f'Your bmi is {bmi}, You are overweight')
else:
    print(f'Your bmi is {bmi}, You are clinically obese')