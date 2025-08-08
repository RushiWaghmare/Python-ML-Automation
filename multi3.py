import multiprocessing



def Evendisplay(n): #siblings
    print("list of even no: ")
    x=2
    for i in range(n):
        print(x)
        x=x+2
def odddisplay(n): #sibling
    print("list of odd no: ")
    x=1
    for i in range(n):
        print(x)
        x=x+2   

def main(): #parent and cmp is parent of parent
    print("Enter number: ")
    value=int(input())
    p1=multiprocessing.Process(target=Evendisplay,args=(value,))
    p2=multiprocessing.Process(target=odddisplay,args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of Program")
if __name__ == "__main__":
    main()