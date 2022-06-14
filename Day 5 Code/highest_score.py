# You are going to write a program that calculates the highest score from a list of scores
# e.g student scores = [78, 65, 89, 55, 91, 64, 89]
# Should not use max or min functions
# Output : The highest score in the class is X

#Write your code below 

student_scores = [78, 65, 89, 55, 91, 64, 89]

score = 0
for scores in student_scores:
    if scores > score:
        score = scores

print(f'The highest score in the class: {score}')
