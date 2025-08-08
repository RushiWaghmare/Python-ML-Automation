import multiprocessing
import os
import threading


def Evendisplay(n): #siblings
    print("PID fo even process",os.getpid())
    print("TID of even Thread:",threading.get_ident())
    print("list of even no: ")
    x=2
    for i in range(n):
        print(x)
        x=x+2


def odddisplay(n): #sibling
    print("PID fo odd process",os.getpid())
    print("TID of odd Thread:",threading.get_ident())
    print("list of odd no: ")
    x=1
    for i in range(n):
        print(x)
        x=x+2   

        

def main(): #parent and cmp is parent of parent
    print("PID fo main process",os.getpid())
    print("TID of main Thread:",threading.get_ident())
    print("Enter number: ")
    value=int(input())

    p1=threading.Thread(target=Evendisplay,args=(value,))
    p2=threading.Thread(target=odddisplay,args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of Program")
if __name__ == "__main__":
    main()