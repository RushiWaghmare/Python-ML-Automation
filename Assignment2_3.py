def factorial(n):
    fact=1
    if n<0:
        print("factorial doesn't exits")
    elif n==0:
        print("Factorial is 1")
    else:
        for i in range(1,n+1):
            fact=fact*i
        print("Factorial of",n,"is",fact)
    

def main():
    a=int(input("Enter number for finding factorial:"))
    factorial(a)
if __name__ == "__main__":
    main()
