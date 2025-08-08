def addition(data):
    sum=0
    for no in data:
        sum=sum+no
    return sum


def main():
    arr=list()
    size=int(input("Enter the size of list: "))
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)
    Result=addition(arr)
    print("Addition of given list integers is : ",Result)


   
   
if __name__ == "__main__":
    main()