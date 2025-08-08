class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        return sum(self.Factors())

    def ChkPerfect(self):
        return self.SumFactors() == 2 * self.Value

def main():
    # Creating multiple objects of the Numbers class
    num1 = Numbers()
    num2 = Numbers()

    # Calling instance methods for each object
    print("For number", num1.Value)
    print("Is prime?", num1.ChkPrime())
    print("Is perfect?", num1.ChkPerfect())
    print("Factors:", num1.Factors())
    print("Sum of factors:", num1.SumFactors())

    print("\nFor number", num2.Value)
    print("Is prime?", num2.ChkPrime())
    print("Is perfect?", num2.ChkPerfect())
    print("Factors:", num2.Factors())
    print("Sum of factors:", num2.SumFactors())

if __name__ == "__main__":
    main()
