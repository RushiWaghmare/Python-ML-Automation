#function defination
def addition(no1,no2):
    ans=0
    ans=no1+no2
    return ans

#function input

a=int(input("Enter the 1st no: "))  
b=int(input("Enter 2nd no: "))

#function calling
result=addition(a,b)
print("addition is :",result)