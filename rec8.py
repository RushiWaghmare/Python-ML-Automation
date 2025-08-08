it will print 1 to 10 digit in decending order
i=1
def DisplayR(n):
        global i
        if(n>=1):
            print(n)
            n=n-1
            DisplayR(n)
        
def main():
    a=int (input("Enter the last digit:"))
    DisplayR(a)
    
if __name__ == "__main__":
    main()