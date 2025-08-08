
    
def main():
    a=int(input("Enter the size of list:"))
    list=[]
    print("Enter the number here:")
    for a in range (a):
        x=str(input("Enter the list numbers:"))
        list.append(x)

    count=0
    for char in list:
        if('a'<=char<='z'):
            count=count+1
             
    print("count of small elements is:  ",count)  
    
    print(list)

if __name__ == "__main__":
    main()