#multicore programing
import multiprocessing
import os
def Cube(n):
    print("PID is : ",os.getpid())
    return n*n*n

def main(): #parent and cmp is parent of parent
   
    arr=[10,20,30,40]
    result=[]
    
    p= multiprocessing.Pool()
    result=p.map(Cube,arr)
    p.close()
    p.join()
    
    print(result)
   

    print("End of Program")
if __name__ == "__main__":
    main()