# Paint area calculator
import math

test_h = int(input('Height of wall: '))
test_w = int(input('Width of wall: '))
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((test_h * test_w)/coverage)
    print(f'Number of paint cans required {number_of_cans}')

paint_calc(height=test_h, width=test_w, cover=coverage)