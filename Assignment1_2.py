def ChkNum(no):
    if(no%2==0):
        print("Even number")
    else:
        print("odd number")

def main():
    n=int(input("Enter number: "))
    ChkNum(n)
if __name__ == "__main__":
    main()