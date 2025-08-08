def addDig(n):
    
    b=1;
    for i in range (1,n+1):
        for j in range(i):
            print(b, end = " ")
        #n=n+1
        b=b+1
        
        
        print("\n")

    
def main():
    a=int(input("Enter the number for addition: "))
    addDig(a)
if __name__ == "__main__":
    main()