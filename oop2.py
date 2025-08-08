

class Demo:
    data1=11        #class variable
    data2=21        #class variable

    def __init__(self,A,B): #parameterized constructor
        print("Inside constructor")
        self.no1=A  #instance variable
        self.no2=B  #instance variable
    
    def Display(self):
        print("value fo no1 from display: ",self.no1)
        print("value fo no2 from display: ",self.no2)
        print("value fo data1 from display: ",Demo.data1)
        print("value fo data2 from display: ",Demo.data2)
    
    @classmethod #decorator
    def fun(cls): #class method
        print("value of Data1 from Fun: ",Demo.data1)
        print("value of Data2 from Fun: ",Demo.data2)
    
    @staticmethod
    def gun():  #static method
        print("inside static methods")

Demo.fun()
Demo.gun()
obj1 = Demo(5,10)
obj1.Display()

