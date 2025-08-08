def addDig(n):
    for i in range(n):
        n=n%10
        x=n/10
        
    
    print(n)
    
def main():
    a=int(input("Enter number: "))
    addDig(a)
if __name__ == "__main__":
    main()