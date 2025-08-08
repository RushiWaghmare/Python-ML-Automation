def loop1(n):
    print("for loop")
    for i in range(n):
        
        print(i)
def loop2(n):
    print("while loop")
    i=1
    while(i<=n):
        print(i)
        i=i+1

def main():
    a=int(input())
    loop1(a)
    loop2(a)
if __name__ == "__main__":
    main()