#Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'{formated_f_name} {formated_l_name}'

formatted_name = (format_name(input('What\'s your first name: '),
input('What\'s your last name: ')))
print(formatted_name)