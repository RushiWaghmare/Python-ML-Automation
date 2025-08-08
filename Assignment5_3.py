i=1
def pattern(n):
    global i
    #for i in range (0,n):  #n=5
    if(i<=n):
        print(n, end = " ")
        n=n-1
        pattern(n)

def main():
    a=int(input("Enter the number: "))
    pattern(a)
if __name__ == "__main__":
    main()