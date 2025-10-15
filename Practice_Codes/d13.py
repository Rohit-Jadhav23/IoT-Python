#set #list #tuple #dictionary are four type of collections in python
def function1():
    s1 = {10, 20, 30, 40, 50}

    print(f"s1= {s1}")
    
function1()


# set
# duplicate values are not allowed

def function1():
    s1 = {10, 20, 30, 40}

    print(f"s1 = {s1}")

    # s1.add(50)
    s1.add(40)

    print(f"After s1 = {s1}")

# function1()


def function2():
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50 ,60}

    print(f"s1 = {s1}")
    print(f"s2 = {s2}")

    print(f"union = {s1.union(s2)}")
    print(f"intersection = {s1.intersection(s2)}")

function2()