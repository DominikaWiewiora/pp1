import re
with open('grades.txt', 'r') as student_grades:
    text = student_grades.read()
    grades = re.findall(r'\d+\.\d+', text)
    grades=[float(grad) for grad in grades]
    mean= sum(grades)/len(grades)
    print(f'{mean:.2f}')
    