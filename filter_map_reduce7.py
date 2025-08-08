from functools import reduce

cheakeven = lambda n: (n % 2 == 0)
Increase = lambda n: n + 1
Add = lambda a, b: a + b

def filterX(Task, Elements):
    result = []
    for no in Elements:
        if Task(no) == True:
            result.append(no)
    return result

def mapX(Task, Elements):
    result = []
    for no in Elements:
        ret = Task(no)
        result.append(ret)
    return result

def main():
    data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list: ", data)

    Fdata = list(filterX(cheakeven, data))
    print("Data after filter activity: ", Fdata)

    Mdata = list(mapX(Increase, Fdata))
    print("Data after Map activity: ", Mdata)

    Rdata = reduce(Add, Mdata)
    print("Data after addition: ", Rdata)

if __name__ == "__main__":
    main()
