class BookStore:
    NoOfBooks =0
    def __init__ (self):
        self.Name=0
        self.Author=0   
        BookStore.NoOfBooks+=1
    def Accept(self):
        self.Name=str(input("Enter the Name of Book : "))
        self.Author=str(input("Enter the of Author : "))

    def Display(self):
        print(self.Name,"By",self.Author)
        print("No of Books : ",BookStore.NoOfBooks)
        

def main():
    coustomer1=BookStore()
    coustomer1.Accept()
    coustomer1.Display()
    print("\n")
    coustomer2=BookStore()
    coustomer2.Accept()
    coustomer2.Display()
if __name__ == "__main__":
    main()
    

    