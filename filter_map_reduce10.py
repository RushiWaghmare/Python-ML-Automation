#using lambda function
import MarvellousFMR as M
cheakeven=lambda n : (n%2==0)

Increase =lambda n:  n+1

Add =lambda a,b : a+b

#user defined funciton for filter,map and reduce

def main():
    data=[]
    print("Enter no of elemnets:")
    size=int(input())

    print("Enter the elements:")
    iCnt=0
    for iCnt in range(0,size):
         
        no=int(input())
        data.append(no)

    print("Data from input list: ",data)


    Fdata=list(M.filterX(cheakeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata=list(M.mapX(Increase,Fdata))
    print("Data after Map activity: ",Mdata)

    
    Rdata =M.reduceX(Add, Mdata)
    print("Data after addition: ",Rdata)

if __name__ == "__main__":
    main()

#Data from input list:  [11, 14, 20, 23, 18, 16, 15, 20]
#Data after filter activity:  [14, 20, 18, 16, 20]
#Data after Map activity:  [15, 21, 19, 17, 21]
#Data after addition:  93