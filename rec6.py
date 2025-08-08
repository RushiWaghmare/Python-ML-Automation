i=1
def DisplayR():
    global i #global means accesible throuout program
    
    # we are using iterative approach to use
    # recursion method
    if(i<=5):
        print(i)
        i=i+1
        DisplayR()
        
def main():
   DisplayR()
    
if __name__ == "__main__":
    main()