
# function definition
def function1():
    print("This is parameter less function")

# function calling
# function1()


def function2(p1):
    print(f"parameter : {p1}")
    print(f"type of p1 = {type(p1)}")

# function2(10)
# function2(3.142) 
# function2('sunbeam')

def function3(p1, p2):
    return p1 + p2

# sum = function3(10, 20)
# sum = function3(10.5, 20.5)
# sum = function3("sun", "beam")
#sum = function3("sun", 10)       ## error

print(f"sum = {sum}")
print(f"type of sum = {type(sum)}")