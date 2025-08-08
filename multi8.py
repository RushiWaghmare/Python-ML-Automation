#multicore programing
import os

def Cube(n):
    print("PID is : ",os.getpid())
    return n*n*n

def main(): #parent and cmp is parent of parent
   
    arr=[10,20,30,40]
    result=[]
    for i in arr:
        result.append(Cube(i))
    
    print(result)
   

    print("End of Program")
if __name__ == "__main__":
    main()