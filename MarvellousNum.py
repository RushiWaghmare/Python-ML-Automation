def ChkPrime(no):
    if no <=1:
        return False
    elif no <=3:
        return True
    elif no%2==0 or no%3==0:
        return False
    else:
        return True







