#multiple calueas return
def calculation(no1,no2):
    add=no1+no2
    sub=no1-no2
    return add,sub
    
    
a=int(input("first value : "))

b=int(input("second value : "))

result1,result2 =calculation(a,b)
print("addition is :",result1)
print("substraction is :",result2)    