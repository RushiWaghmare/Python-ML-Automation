def maximum(data):
    max_int=data[0]
    for no in data:
        if no>max_int:
            max_int =no
    return max_int
    

def main():
    arr=list()
    size=int(input("Enter the size of list: "))
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)
    result1=maximum(arr)
 

    print("maximum no from list is: ",result1)
   


   
   
if __name__ == "__main__":
    main()