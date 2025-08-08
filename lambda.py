# Syntax:
#Name = lambda Parameters : Logic
#Name (___,___,...)
def addition(a,b):
    ans=0
    ans=a+b
    return ans
#lambda function:
Add=lambda a,b: a+b
def main():
    ret= addition(10,11)
    print("addition is : ",ret)

if __name__ == "__main__":
    main()