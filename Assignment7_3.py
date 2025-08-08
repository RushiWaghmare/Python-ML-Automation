class Arithmetic:
    result=0
    def __init__ (self):
        self.value1=0
        self.value2=0
        self.value3=0

    def Accept(self):
        self.value1=int(input("Enter first no: "))
        self.value2=int(input("Enter second no: "))
    
    def Addition(self):
        Arithmetic.result=self.value1 +self.value2
        print("Addition of given values is: ",Arithmetic.result)
        
    def Substraction(self):
        Arithmetic.result=self.value1 -self.value2
        print("Substraction of given values is: ",Arithmetic.result)
    
    def Multipliction(self):
        Arithmetic.result=self.value1 *self.value2
        print("Substraction of given values is: ",Arithmetic.result)

    def Division(self):
        Arithmetic.result=self.value1 /self.value2
        print("Substraction of given values is: ",Arithmetic.result)

def main():
    
    obj1=Arithmetic()
    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multipliction()
    obj1.Division()

    print("\n")

    obj2=Arithmetic()
    obj2.Accept()
    obj2.Addition()
    obj2.Substraction()
    obj2.Multipliction()
    obj2.Division()

if __name__ == "__main__":
    main()
