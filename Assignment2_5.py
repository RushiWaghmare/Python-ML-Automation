def prime(n):
    if n<=1:
        print("not prime")
    elif n<=3:
        print("prime")
    elif n%2 == 0 or n%3 == 0:
        print("not prime")
    else:
        print("prime")
        
                

def main():
    a=int(input("Enter the no to cheak Prime: "))
    prime(a)
if __name__ == "__main__":
    main()