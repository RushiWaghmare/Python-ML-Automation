def cheakfreq(data,target):
    frequnecy= data.count(target)
    return frequnecy
    
def main():
    arr=list()
    size=int(input("Enter the size of list: "))
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)
    
    n=int(input("Enter the number you want to cheak frequnecy from given list: "))
    
    freq=cheakfreq(arr,n)
    print("frequency of",n,"is",freq)

   
   
if __name__ == "__main__":
    main()