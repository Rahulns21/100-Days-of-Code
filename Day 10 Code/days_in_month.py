#Function to find number of days in a month

def days_in_month(month):
    '''Returns the number of days in a entered month'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return 'Invalid month!'
    return month_days[month-1]

result = days_in_month( int(input('Enter a month: ')))
print(result)