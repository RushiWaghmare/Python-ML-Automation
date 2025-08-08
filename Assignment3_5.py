import MarvellousNum as M
def ListPrime(data):
    prime_sum=0
    for no in data:
        if M.ChkPrime(no):
            prime_sum=prime_sum +no
    return prime_sum


def main():
    arr=list()
    size=int(input("Enter the size of list: "))
    for i in range(size):
        no=int(input())
        arr.append(no)
    print(arr)

    
    result1=ListPrime(arr)
    print("addition of all prime numbers form list is: ",result1)



if __name__ == "__main__":
    main()