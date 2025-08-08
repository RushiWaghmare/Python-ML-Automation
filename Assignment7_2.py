class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumferance=0.0

    def Accept(self):
        self.Radius=float(input("Enter the radius of Circle : "))

    def CalculateArea(self):
        self.Area= Circle.PI* self.Radius* self.Radius
        
    def CalculateCircumference(self):
        self.Circumferance= 2*Circle.PI * self.Radius

    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: ",self.Area)
        print("Circumferance: ",self.Circumferance)
def main():

    #object of Circle is circle1
    circle1 = Circle()

    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()
    print("\n")
    circle2 = Circle()
    circle2.Accept()
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    circle2.Display()

if __name__ == "__main__":
    main()

