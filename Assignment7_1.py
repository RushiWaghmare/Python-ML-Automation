class Demo:
    value=0
    
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Fun(self):
        print("value no1 is form Fun : ",self.no1)
        print("value no2 is from Fun :",self.no2)

    def Gun(self):
        print("value no1 is form Gun : ",self.no1)
        print("value no2 is from Gun :",self.no2)
    

def main():

    obj1= Demo(11,21)
    obj2=Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()
if __name__ == "__main__":
    main()