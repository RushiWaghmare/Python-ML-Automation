#user will use this file
from marvellous import Addition
from marvellous import multiplication

def main():
    print("Enter first number: ")
    a=int(input())
    
    print("Enter first number: ")
    b=int(input())
    
    ans=Addition(a,b)
    print(ans)
    ans=multiplication(a,b)
    print(ans)
    
main()

    
