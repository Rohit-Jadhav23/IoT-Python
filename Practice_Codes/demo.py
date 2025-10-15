
# List
# collection of similar or dissimilar type of data
# mutable

def function1():
    # l1 = []         # empty list
    # l1 = list()     # empty list

    l1 = [11, 22, 33, 44, 55]

    # print(l1)

    # for ele in l1:
    #    print(ele)

    print(f"l1[0] = {l1[0]}")
    print(f"l1[3] = {l1[3]}")

    print(f"length : {len(l1)}")
    print(f"index of 44 : {l1.index(44)}")


def function2():
    l1 = [11, 22, 33, 44, 55, 66]

    print(f"List before : {l1}")

    # l1.append(77)       # append 77 at the end of list
    # l1.insert(1, 100)       # 100 will be inserted at 1 index

    # l1.pop()                # remove last element from the list
    # l1.pop(2)                  # remove element of 2nd index

    l1.remove(44)           # 44 will be removed from list

    print(f"List after : {l1}")




def function3():
    student = ["abc", 120, 65.5]

    # print(student)
    print(f"name = {student[0]}, rollno = {student[1]}, marks = {student[2]}")

function3()
function1()
function2()

