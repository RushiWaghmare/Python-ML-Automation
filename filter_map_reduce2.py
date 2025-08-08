from functools import reduce
def cheakeven(n):
    return(n%2==0)

def Increase(n):
    return n+1

def Add(a,b): 
    return a+b
def main():
    data=[11,14,20,23,18,16,15,20]
    print("Data from input list: ",data)


    Fdata=list(filter(cheakeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata=list(map(Increase,Fdata))
    print("Data after Map activity: ",Mdata)

    Rdata =reduce(Add, Mdata)
    print("Data after addition: ",Rdata)

if __name__ == "__main__":
    main()

#Data from input list:  [11, 14, 20, 23, 18, 16, 15, 20]
#Data after filter activity:  [14, 20, 18, 16, 20]
#Data after Map activity:  [15, 21, 19, 17, 21]
#Data after addition:  93