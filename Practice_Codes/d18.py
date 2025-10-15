
def function1():
    import mymath

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    sum = mymath.sum(num1, num2)
    diff = mymath.diff(num1, num2)

    print(f"sum = {sum}, diff = {diff}")
    print(f"PI = {mymath.PI}")

# function1()

def function2():
    import mymath as m

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    sum = m.sum(num1, num2)
    diff = m.diff(num1, num2)

    print(f"sum = {sum}, diff = {diff}")
    print(f"PI = {m.PI}")

# function2()

def function3():
    from mymath import sum
    from mymath import diff

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    sum = sum(num1, num2)
    diff = diff(num1, num2)

    print(f"sum = {sum}, diff = {diff}")
    # print(f"PI = {mymath.PI}")

function3()

def function4():
    from mymath import sum as add
    from mymath import diff as sub

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    sum = add(num1, num2)
    diff = sub(num1, num2)

    print(f"sum = {sum}, diff = {diff}")
    # print(f"PI = {mymath.PI}")

function4()