from functools import reduce

def cheakno(no):
    if no <= 1:
        return False
    elif no <= 3:
        return True
    elif no % 2 == 0 or no % 3 == 0:
        return False
    else:
        return True

def Increase(no):
    return no * 2

def my_max(no):
    maximum = 0
    for i in no:
        if i > maximum:
            maximum = i
    return maximum

def main():
    arr = []
    n = int(input("Enter the size of list: "))
    for i in range(n):
        a = int(input())
        arr.append(a)

    print("Given list is: ", arr)
    elearr1 = list(filter(cheakno, arr))
    print("List after Filter: ", elearr1)

    elearr2 = list(map(Increase, elearr1))
    print("List after Map: ", elearr2)

    elearr3 = reduce(my_max, elearr2)
    print("List after Reduce: ", elearr3)

if __name__ == "__main__":
    main()
