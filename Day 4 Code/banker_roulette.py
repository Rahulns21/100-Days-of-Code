import random


names_string = input('Give me everybody\'s names, seperated by a comma: ')
names = names_string.split(',')
print(random.choice(names) + ' is going to buy the meal today')
