#addition of each digit from givne input

i=1
sum=0
def pattern(n):
    global i
    global sum
    
    if n<=0:
        return n
    else:
        sum=n%10 + pattern(n//10)
        return sum


def main():
    a=int(input("Enter the number: "))
    result=pattern(a)
    print("sum of all digit is : ",result)
if __name__ == "__main__":
    main()
   
   