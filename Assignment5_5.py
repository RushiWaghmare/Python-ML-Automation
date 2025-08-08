def factor(n):
    
    if n <=2:
        return n
    else:
        fact=n* factor(n-1)
        return fact

    

def main():
    a=int(input("Enter the number: "))
    result=factor(a)
    print(result)
if __name__ == "__main__":
    main()