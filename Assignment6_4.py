import threading

def small(list):
    count=0
    for char in list:
        if('a'<=char<='z'):
            count=count+1
             
    print("count of Small elements is:  ",count)  
    

def capital(list):
    count=0
    for char in list:
        if('A'<=char<='A'):
            count=count+1
             
    print("count of Capital elements is:  ",count)  
   
def digit(list):
    count=0
    for char in list:
        if('0'<=char<='9'):
            count=count+1
             
    print("count of Digits is:  ",count)  
   

    
def main():
    
    a=int(input("Enter the size of list:"))
    list=[]
    print("Enter the number here:")
    for i in range(a):
        x=str(input())
        list.append(x)
    print(list)


    p1= threading.Thread(target = small, args=(list,))
    p2= threading.Thread(target = capital, args=(list,))
    p3= threading.Thread(target = digit, args=(list,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()