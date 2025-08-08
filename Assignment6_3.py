import threading
def evenlist(list):
    sum=0
    for i in list:
        if( i%2 == 0 ): 
            sum = sum+i
    print("additon of all even element are:",sum)

def oddlist(list):
    sum=0
    for i in  list:
        if( i%3 == 0 ):
            sum = sum+i
    print("additon of all odd element are:",sum)
    
def main():
    a=int(input("Enter the size of list:"))
    list=[]
    print("Enter the number here:")
    for i in range(a):
        x=int(input())
        list.append(x)
    print(list)
    p1= threading.Thread(target = evenlist, args=(list,))
    p2= threading.Thread(target = oddlist, args=(list,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Exit from main")
if __name__ == "__main__":
    main()