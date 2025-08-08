#factorial of 5 is : 5*4*3*2*1=120
fact=1
i=1
def factorial(n):
        global i
        global fact

        if(n >= 1): #6
            fact=fact*n
            n=n-1
            factorial(n)
        return fact
        
def main():
    a=int (input("Enter the last digit:"))
    ret=factorial(a)
    print("factoral is: ",ret)
    
if __name__ == "__main__":
    main()