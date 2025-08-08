import sys

def addition(x, y):
    ans = x + y
    return ans

def main():
    print("Welcome to additon"+sys.argv[0])

    if (len(sys.argv) != 3 ):
        print("Invalid Arguments")
        print("Please provide 2 arguments for additon")
        return

    result= addition(int(sys.argv[1]), int(sys.argv[2]))
    print(result)


if __name__  =="__main__":
    main()