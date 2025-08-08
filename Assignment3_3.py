def minimum(data):
    min_int=data[0]
    for no in data:
        if no<min_int:
            min_int = no
    return min_int

def main():
    arr=list()
    size=int(input("Enter the size of list: "))
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)
 
    result2=minimum(arr)

   
    print("minimum no from list is:",result2)


   
   
if __name__ == "__main__":
    main()