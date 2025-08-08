def addition(data):
    sum=0
    for no in data:
        sum=sum+no
    return sum

def main():
    print("Enter the no of elements in list:")
    size=int (input())
    Arr=list()
    
    print(" Enter size of list:")
    
    for i in range(size):
        no= int(input())
        Arr.append(no)
        
    print("Entered elements are :", Arr)
    
    Result = addition (Arr)
    print("Addition of given list value is:",Result)
if __name__ =="__main__":
    main()