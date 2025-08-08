import sys  #system module 

def main():

#python command2.py   marvellous 21 Pune

    print("Demonstration of Commmandline argument")
    print("name of application", sys.argv[0])  # command2.py
   # print("first index ",sys.argv[1])   #marvellous
    #print("second index ",sys.argv[2])  #21
    #print("Thired index ",sys.argv[3])  #Pune

    print("Data type of argv is ", type(sys.argv))  #Data type of argv is  <class 'list'>

    print("No of command line arguments are",len(sys.argv)) #No of command line arguments are 4 --> by default is 1





if __name__ == "__main__":
    main()