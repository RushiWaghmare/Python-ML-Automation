#function defination
def addition(no1,no2):#6
    ans=0
    ans=no1+no2
    return ans #7

#entry point function
def main():#2
    print("Inside the main fuction !")
    a=int(input("Enter the 1st no: "))  #3
    b=int(input("Enter 2nd no: "))  #4

    #function calling
    result=addition(a,b)    #5
    print("addition is :",result)#8
    
main()# starter to end
print("end of application") # new end





#output
#Inside the main fuction !
#Enter the 1st no: 10
#Enter 2nd no: 20
#addition is : 30
#end of application