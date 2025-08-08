import multiprocessing
import threading

def even(n):
    x=2
    for i in range(n):
        print(x)
        x=x+2

def odd(n):
    x=1
    for i in range(n):
        print(x)
        x=x+2

    
def main():
    value=int(input("Enter number:"))
    p1= threading.Thread(target = even, args=(value,))
    p2= threading.Thread(target = odd, args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of Program")

if __name__ == "__main__":
    main()