import sys
def addition (no1,no2):
    ans =no1+no2
    return ans

def main():
    print("welcome to the application:"+sys.argv[0])
    
    if (len(sys.argv) !=3):
        print("invalid numberof argument")
        print("please provid 2 numeric argument to prform addition")
        
        return
        
    Result = Addition(int (sys.argv[1],int (sys.argv[2])))
    print(Result)
    
if __name__ == "__main__":
    main()