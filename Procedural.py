print("Demonstration of Procedural")

def Addition(n1,n2):
    ans=n1+n2
    return ans

def Substraction(n1,n2):
    ans=n1-n2
    return ans

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    resutl1= Addition(a,b)
    print(resutl1)

    resutl2=Substraction(a,b)
    print(resutl2)
if __name__ == "__main__":
    main()