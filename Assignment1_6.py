def number(no):
    if no>0:
        print("Postive number")
    elif no<0:
        print("Negative number")
    else:
        print("Zero")

def main():
    n=int(input("Enter number:"))
    result=number(n)
    
if __name__ == "__main__":
    main()