def greet():
    print('Hello World')
    print('I love to code')
    print('I like python')

greet()

#Function that allows for input

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How are you {name}?')

greet_with_name('Rahul')

#Function with more than one input

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'How\'s the weather in {location}')

greet_with('Rahul', 'Bangalore')
