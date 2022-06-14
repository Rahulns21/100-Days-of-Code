student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
students = 0
for height in student_heights:
    total_height += height

for student in student_heights:
    students += 1

average_height = str(total_height/students)
print('Average height of students: '+ average_height)