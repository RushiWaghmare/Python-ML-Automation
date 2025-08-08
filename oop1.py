

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

obj1 = Demo(5,10)
obj2 = Demo(15,20)

print("value fo no1 form obj1: ",obj1.no1)
print("value fo no2 form obj1: ",obj1.no2)

print("value fo no1 form obj2: ",obj2.no1)
print("value fo no2 form obj2: ",obj2.no2)

print("value of Data1: ",Demo.data1)
print("value of Data2: ",Demo.data2)

print("--------------------------------------------")

obj1.Display() #display is instance of class demo that why we use its object
obj2.Display()