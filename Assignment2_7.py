def NoPattern(n):
     b=1;
     for i in range (n):
        for j in range(n):
            print(b, end = " ")
        b=b+1
        
        print("\n")

def main():
    a=int (input("Enter Number: "))
    NoPattern(a)
if __name__ == "__main__":
    main()