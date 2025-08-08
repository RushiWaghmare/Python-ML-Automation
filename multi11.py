#without multicore programing
import multiprocessing
import os
import time
def fun(n):
    sum=0
    print("PID is : ",os.getpid())
    for i in range(n):
        sum=sum+(n*n*n)
    return sum

def main(): #parent and cmp is parent of parent
    starttime=time.time()
    arr=[100000,2000000,300000,400000,500000,600000,700000,800000,900000,100000,1100000,1200000,1300000,1400000]
    result=[]
    
    for i in arr:
        result.append(fun(i))
    
    print(result)
    endtime=time.time()
    print("time requred for execution: ",endtime-starttime)

    print("End of Program")
if __name__ == "__main__":
    main()