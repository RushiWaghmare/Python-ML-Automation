class BankAccount:
    ROI = 10.5
    
    def __init__ (self):
        self.Name = ""
        self.Amount = 0
        self.remaining = 0
        self.interest = 0
    
    def Deposit(self):
        self.Name = input("Enter your name: ")
        self.Amount = int(input("Enter the amount to deposit: "))

    def Withdraw(self):
        withdrawal = int(input("Enter the amount to withdraw: "))
        self.remaining = self.Amount - withdrawal
        print("The amount remaining after withdrawal:", self.remaining)
    
    def CalculateInterest(self):
        self.interest = (self.Amount * BankAccount.ROI) / 100
        print("The interest on the given amount is: Rs", self.interest)

    def Display(self):
        print("Name:", self.Name)
        print("Amount deposited:", self.Amount)

def main():
    customer1 = BankAccount()
    customer1.Deposit()
    customer1.Withdraw()
    customer1.Display()
    customer1.CalculateInterest()

if __name__ == "__main__":
    main()
