
# list of tuples

def function1():
    students = [
        (1, "abc", 4, 98.0),
        (2, "xyz", 3, 89.5),
        (3, "mno", 6, 80.0),
        (4, "pqr", 5, 79.7)
        ]
    
    print(students)

# function1()

def function2():
    students = [
        (1, "abc", 4, 98.0),
        (2, "xyz", 3, 89.5),
        (3, "mno", 6, 80.0),
        (4, "pqr", 5, 79.7)
        ]
    
    for student in students:
        print(student)

# function2()

def function3():
    students = [
        (1, "abc", 4, 98.0),
        (2, "xyz", 3, 89.5),
        (3, "mno", 6, 80.0),
        (4, "pqr", 5, 79.7)
        ]
    
    for student in students:
        print(f"rollno = {student[0]}, name = {student[1]}, std = {student[2]}, marks = {student[3]}")

function3()

def function4():
    students = [
        (1, "abc", 4, 98.0),
        (2, "xyz", 3, 89.5),
        (3, "mno", 6, 80.0),
        (4, "pqr", 5, 79.7)
        ]
    
    for (rollno, name, std, marks) in students:
        print(f"rollno = {rollno}, name = {name}, std = {std}, marks = {marks}")

function4()