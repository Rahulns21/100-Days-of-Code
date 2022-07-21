#Functions with multipe returns

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return 'You did\'t provide valid input.'
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'{formated_f_name} {formated_l_name}'

formatted_name = (format_name(input('What\'s your first name: '),
input('What\'s your last name: ')))
print(formatted_name)