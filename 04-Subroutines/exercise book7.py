def computegrade():
    grade=float(input('Enter grade: '))
    if grade>=0.9:
            grade='A'
    elif grade<0.9 and grade>=0.8:
            grade='B'
    elif grade<0.8 and grade>=0.7:
            grade='C'
    elif grade<0.7 and grade>=0.6:
            grade='D'
    else:
            grade=='F'
    if grade not in ['A','B','C','D','F']:
           return 'Bad score'
    return grade
x=computegrade()
print(x)
    
        