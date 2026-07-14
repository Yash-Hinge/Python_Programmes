def CountCapital(Brr):

    CntCap =0

    for ch in Brr:
         if(ord(ch)>=65 and ord(ch)<=90):    
             CntCap=CntCap+1

    return CntCap


def Main(): 
    print("Enter the String :")
    Arr = input()

    Ret = CountCapital(Arr)

    print ("The Number of capital charracters in the string are :",Ret)
Main()
 