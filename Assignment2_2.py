def pattern(n):
     for i in range(n):
        for j in range (n):
            print("*",end = " ")
        print("\n")
def main():
    a=int (input("Enter number for pattern printing:"))
    pattern(a)
   
if __name__ == "__main__":
    main()