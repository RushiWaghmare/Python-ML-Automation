import Arithmetic as A

def main():
    print("Enter values given below")
    a=int(input("first no: "))
    b=int(input("second no: "))

    result1=A.Add(a,b)
    print(result1)

    result2=A.Sub(a,b)
    print(result2)

    result3=A.Mult(a,b)
    print(result3)

    result4=A.Div(a,b)
    print(result4)

if __name__ == "__main__":
    main()
    