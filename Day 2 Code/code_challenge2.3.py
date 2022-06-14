#2.3 code challenge - No of Days and Weeks left

# Take user input
age = input('What is your current age? ')

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

result = (f'You have {days_remaining}, {weeks_remaining} weeks, and {months_remaining} months left')
print(result)