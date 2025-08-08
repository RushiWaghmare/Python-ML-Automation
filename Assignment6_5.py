import threading

def thread1(n):
    for  i in range(n+1):
        print(i)
        i=i+1
    

def thread2(n):
    for  i in range(n):
        print(n)
        n=n-1
    

    
def main():
    a=int(input("Enter the total digit you want to print: "))
    p1= threading.Thread(target = thread1, args=(a,))
    p2= threading.Thread(target = thread2, args=(a,))

    p1.start()
    p1.join()

    print("thread 2 after Execution of thread 2")

    p2.start()
    p2.join()

    print("Exit form main")

if __name__ == "__main__":
    main()