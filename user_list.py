

def main():
    print("Enter the no of elements in list:")
    size=int (input())
    Arr=list()
    
    print(" Enter the elements:")
    
    for i in range(size):
        no= int(input())
        Arr.append(no)
        
    print("Entered elements are :", Arr)
if __name__ =="__main__":
    main()