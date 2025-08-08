#variable no of argument function(no of parameters)
def addition(*no):
    print(type(no))
    print(len(no))
    ans=0
    
    for i in no:
        ans=ans+i
        
    return ans
    


def main():
    result=addition(1,2,3)
    result2=addition(1,2,3,4)
    result3=addition(1,2,3,5)
    print(result)
    print(result2)
    print(result3)
    
    
if __name__ == "__main__":
    main()