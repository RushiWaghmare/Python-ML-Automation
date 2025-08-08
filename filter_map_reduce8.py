#using lambda function

cheakeven=lambda n : (n%2==0)

Increase =lambda n:  n+1

Add =lambda a,b : a+b

#user defined funciton for filter,map and reduce

def filterX(Task,Elements):
    result= []
    for no in Elements:
        if(Task(no)== True):
            result.append(no)
    return result

def mapX(Task,Elements):
    result=[]
    for no in Elements:
        ret=Task(no)
        result.append(ret)

def reduce(Task,Elements):
    sum=0
    for no in Elements:
        sum=Task(sum,no) # it will call add funtion
    return sum


def main():
    data=[11,14,20,23,18,16,15,20]
    print("Data from input list: ",data)


    Fdata=list(filterX(cheakeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata=list(mapX(Increase,Fdata))
    print("Data after Map activity: ",Mdata)

    
    Rdata =reduceX(Add, Mdata)
    print("Data after addition: ",Rdata)

if __name__ == "__main__":
    main()

#Data from input list:  [11, 14, 20, 23, 18, 16, 15, 20]
#Data after filter activity:  [14, 20, 18, 16, 20]
#Data after Map activity:  [15, 21, 19, 17, 21]
#Data after addition:  93