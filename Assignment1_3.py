def Add(no1,no2):
    addition=0
    addition=no1+no2
    return addition 
def main():
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))

    result=Add(n1,n2)
    print("The addition of given numbers is :",result)
if __name__ == "__main__":
    main()