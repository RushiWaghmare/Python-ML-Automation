def evenodd(n):
    return n%2 == 0
    #if(n%2 == 0):
     #   return True
    #else:
     #   return False

evenoddX=lambda n:(n%2 ==0)
def main():
  ret=evenoddX(10)
  if(ret == True):
    print("even")
  else:
    print("odd")

if __name__ == "__main__":
    
    
    main()