def factor_add(n):
    result=0
    for i in range(n):
        n=n%10
        result=result+n
        n=n-1
        
    print(result)
    

def main():
    a=int(input("Enter no =: "))
    factor_add(a)
if __name__ == "__main__":
    main()