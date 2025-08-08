def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end =" ")
        n=n-1
        print("\n")

def main():
    a=int (input ("Enter number: "))
    result=pattern(a)
if __name__ == "__main__":
    main()