#using Genral Exception
def main():
    ans=0

    #Exception prone code
    try:
        print("Enter first number:")
        no1=int(input())

        print("Enter second number:")
        no2=int(input())

        ans=no1/no2


    #Exception handler code
    except ZeroDivisionError as zobj:
        print("Exception occured ",zobj)

    except ValueError as vobj:
        print("Exception occured",vobj)

    #Generic Exception handler (bottom) which can work as Parent Exception
    except Exception as eobj:
        print("Exception occured",eobj)


    
    print("Division is: ",ans)



    
if __name__ == "__main__":
    main()