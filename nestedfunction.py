#multiple calculation return

#function defination
def calculation(no1,no2):       #3
    def addition(x,y):          #5          
        return x+y
    
    def substraction(x,y):      #7
        return x-y
    
    #nested function calling
    Ans1=addition(no1,no2)      #4 #all nested function should call
    Ans2=substraction(no1,no2)  #6
    return Ans1,Ans2            #8
 
    
a=int(input("first value : "))   #1
b=int(input("second value : ")) #2

#function calling
result1,result2 =calculation(a,b)   #9
print("addition is :",result1)      #10
print("substraction is :",result2)    #11