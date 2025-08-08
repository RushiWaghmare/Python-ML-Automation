class BankAccount:
    ROI=10.5
    
    def __init__ (self):
        self.Name=0
        self.Ammount=0
        self.remaining=0
        self.intrest=0

    def Deposit(self):
        self.Name=str(input("Enter your name : "))
        self.Ammount=int(input("Enter the amount here to deposit : "))

    def Withdraw(self):
        withdraw=int(input("Enter the amount to be withdrawn : "))
        self.remaining = self.Ammount - withdraw
        print("The ammount  remaining after withdrawn : ",self.remaining)
    
    def CalculateIntrest(self):
        self.intrest=(self.Ammount*BankAccount.ROI)/100
        print("The intrest on given ammount is : Rs ",self.intrest)

    def Display(self):
        print(self.Name)
        print(self.Ammount)

def main():
    coustomer1=BankAccount()
    coustomer1.Deposit()
    coustomer1.Withdraw()
    coustomer1.CalculateIntrest()
    coustomer1.Display()
   

if __name__ == "__main__":
    main()
    

    

