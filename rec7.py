i=1
def DisplayR(n):
        global i
        if(i<=n):
            print(i)
            i=i+1
            DisplayR(n)
        
def main():
    a=int (input("Enter the last digit:"))
    DisplayR(a)
    
if __name__ == "__main__":
    main()