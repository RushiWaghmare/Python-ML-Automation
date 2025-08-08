from functools import reduce
print("demonstration of Filter Map Reduce")

def Evenchk(no):
    return(no%2==0)


def Increase(no):
    return no+2

def Add(a,b):
    return a+b

arr=[ 98,9,5,16,2,4,21,30,11]

evenarr=list(filter(Evenchk,arr))
print("Data after filter",evenarr)

modArray=list(map(Increase,arr))
print("Data after map",modArray)

sum=reduce(Add,modArray)
print("addition of even numbers",sum)

#demonstration of Filter,Map reduce using lambda function

evenArr=list(map(lambda no : (no%2== 0),arr))
print(("Data after filter using lambda",evenArr))

modArray=list(map(lambda no : no+2,evenArr))
print("Data after map using lambda",modArray)

sum=reduce(lambda a,b : a+b,modArray)
print("addition of even numbers using lambda",sum)

#if __name__ == "__main__":
 #   main()