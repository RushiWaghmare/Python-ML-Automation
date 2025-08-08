#using defaul argument
def area(Radius,PI=3.14): 
#if value of PI
#missing in input so we can use default value
# that is 3.14
    Result=Radius*PI*Radius
    return Result

def main():
    ans=area(5)
    print("area of circle is : ",ans)#default will use
    
    ans=area(5,7.20)
    print("area of circle2 is : ",ans)#no need of default
    
    ans=area(Radius=5)
    print("area of circle3 is : ",ans)
    
if __name__== "__main__":
    main()