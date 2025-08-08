import threading
def evenfactor(n):
    fact_sum=0
    for i in range(1,n+1):
        if(n%i == 0 and i%2 == 0 ): #10==2,5,10
            fact_sum = fact_sum+i
    print(fact_sum)

def oddfactor(n):
    fact_sum=0
    for i in range(1,n+1):
        if(n%i == 0 and i%2 != 0 ):#10==
            fact_sum = fact_sum+i
    print(fact_sum)

def main():
    value=int(input("Enter number:"))
    p1= threading.Thread(target = evenfactor, args=(value,))
    p2= threading.Thread(target = oddfactor, args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit form main")

if __name__ == "__main__":
    main()