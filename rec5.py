i=0
def fun():
    global i #global means accesible throuout program
    print("inside the fun")
    i=i+1
    fun()

def main():
    fun()
    
if __name__ == "__main__":
    main()