import os
import multiprocessing as M

def task1(no):
    print(("Execution first taskt"))
    print("PID of task1 : ",os.getpid())        #51
    print("PID of task1 : ",os.getppid())       #11


def task2(no):
    print(("Execution first taskt"))
    print("PID of task2 : ",os.getpid())    #101
    print("PID of task2 : ",os.getppid())   #11


def main():
    print("PID of running process : ",os.getpid())  #11
    print("PID of parent process : ",os.getppid())  #21

    value=11
    p1=M.Process(target= task1,args=(value,))
    p2=M.Process(target= task1,args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()
