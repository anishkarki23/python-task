import math


increment = 1
num_of_student = int(input("Enter number of students"))
student_marks = []

while increment <= num_of_student:
    print(f"======Student No: {increment}========")
    for i in range(1):
        sci = int(input("Enter Science mark: "))
        mat = int(input("Enter Mathematics mark: "))
        soc = int(input("Enter Social Studies mark: "))
        phy = int(input("Enter Physics mark: "))
        eco = int(input("Enter Economics mark: "))
        mark = [sci, mat, soc, phy, eco]
        student_marks.append(mark)
    increment += 1
x = 1
for mark in student_marks:
    total = 0
    for mr in mark:
        total += mr

    per = total / 5
    division = ""

    if per > 34 and per <=45:
        division += "Third Division"
    elif per > 45 and per <= 65:
        division += "Second Division"
    elif per  > 65 and per <= 75:
        division += "First Division"
    elif per > 75 and per <=100:
        division += "Excellent Division"
    elif per > 100:
        division += "Invalid Input"
    else:
        division += "Fail"

    print(f"Student number: {x} percentage: {per} Div:{division}")
    x +=1
