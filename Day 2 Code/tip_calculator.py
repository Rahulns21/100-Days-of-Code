total_bill = float(input('What was the total bill? $'))
percentage_tip = int(input('What percent tip would you like to give? 10, 12, or 15? '))
members = int(input('How many people to split the bill? '))
bill_with_tip = (percentage_tip / 100) * total_bill
single_tip = bill_with_tip / members
divided_bill = total_bill / members
result = round(single_tip + divided_bill, 2)
print(f'Each person should pay: {result}')

