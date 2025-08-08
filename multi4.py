import multiprocessing

def Evendisplay(n):
    print("lis t of  event no: ")
    x=2
    for i in range(n):
        print(x)
        x=x+2
def odddisplay(n):
    print("lis t of  event no: ")
    x=1
    for i in range(n):
        print(x)
        x=x+2   

def main():
    print("Enter number: ")
    value=int(input())
    p1=multiprocessing.Process(target=Evendisplay,args=(value,))
    p2=multiprocessing.Process(target=odddisplay,args=(value,))
    # this is wrong multoprocessing
    p1.start()
    p1.join()

    p2.start()
    p2.join()

    
    
    print("End of Program")
if __name__ == "__main__":
    main()