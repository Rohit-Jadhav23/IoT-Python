
# List of list
def function1():
    l1 = [[1, 2, 3, 4], [10, 20, 30 ,40], [11, 22, 33, 44]]

    print(l1)

    # l1.append([1, 2, 3, 4])
    # l1.append(50)

    print(f"l1[0]= {l1[2]}")

    for l in l1:
        print(l)

    for l in l1:
        for e in l:
            print(f" {e}")

function1()