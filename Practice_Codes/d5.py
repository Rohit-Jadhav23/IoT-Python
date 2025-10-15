
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

max = 0

if num1 == num2:
    print("num1 and num2 are equal")
    max = num1
elif num1 > num2:
    print("num1 is greater than num2")
    max = num1
else:
    print("num2 is greater than num1")
    max = num2


print(f"Maximum value : {max}")