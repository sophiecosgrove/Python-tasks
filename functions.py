def grade(name, homework, assessment, final_exam):
    grade =  homework + assessment + final_exam
    if grade >= 150:
        result = 'A'
    elif grade >= 120:
        result = 'B'
    elif grade >= 90:
        result = 'C'
    elif grade < 60:
        result = 'D'
    return name, 'grade in ICT is:' , result

print(grade(input('What is your name: '), int(input('Enter homework mark /25: ')), int(input('Enter assessment mark /50: ')), int(input('Enter final exam mark /100: '))))