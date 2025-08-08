def CheckEven(No):
    if (No%2==0):
        print("it is even no")
    else:
        print("it is odd no")
        
def main():
    print("Enter number: ")
    a=int(input())
    
    CheckEven(a)
if__name__=="__main__":
main()