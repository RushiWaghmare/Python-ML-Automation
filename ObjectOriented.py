print("Demonstration of Object Orientation")
##########################################################
class Arithmatic:
    def __init__(self,Value1,Value2):
        self.no1=Value1 #characteristic
        self.no2=Value2 #characteristic
    
    def Addition(self): #Behaviour
        ans=self.no1+self.no2
        return ans

    def Substraction(self):
        ans=self.no1-self.no2
        return ans

#############################################################

a=int(input("Enter first number: "))

b=int(input("Enter second number: "))

obj=Arithmatic(a,b)

result=obj.Addition()
print(result)

result=obj.Substraction()
print(result)