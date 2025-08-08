#Predefined function
def sub(a,b):   #0x100
    print(a-b)

#User-defined decorator 
def Smartsub(fptr):     #0x200
    def Inner (a,b):    #0x300
        if a < b:
            a,b = b,a
        return fptr(a,b)
    return Inner            #return 0x300
    

sub=Smartsub(sub)  # calling Smartsub(0x100)

def main(): #0x400
    no1=int(input("Enter first number"))
    no2=int(input("Enter second number"))

    sub(no1,no2) #0x300(1990,1992)


if __name__ == "__main__":
    main()