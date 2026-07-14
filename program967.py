def CountCapital(Brr):

    CntCap =0

    for i in range(len(Brr)):
         if(Brr[i]>='A' and Brr[i]<='Z'):
             CntCap=CntCap+1

    return CntCap


def Main(): 
    print("Enter the String :")
    Arr = input()

    Ret = CountCapital(Arr)

    print ("The Number of capital charracters in the string are :",Ret)
Main()
 