programming_dictionary = {
    'Bug': 'An error in program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.',
    'Loop': 'The action of doing something over and over again'
}

#Retrieving items from dictionary
print(programming_dictionary['Function'])

#Adding new items to dicitionary
programming_dictionary['Python'] =  'A powerful programming language used in many cases'

#Create an empty dictionary
empty_dictionary = {}

#Adding items to empty dictionary
empty_dictionary['Java'] = 'A programming language which runs on 3.2 billion devices'

#Wipe an existing dictionary
# programming_dictionary = {}

#Edit an item in dictionary
#Now bug is assigned with new value
programming_dictionary['Bug'] = 'A moth in your computer' 

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])