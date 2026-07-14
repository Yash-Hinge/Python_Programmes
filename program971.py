def CountCapital(Brr):

    CntCap =0

    for ch in Brr:
         if(ch>=65 and ch<=90):     #issue
             CntCap=CntCap+1

    return CntCap


def Main(): 
    print("Enter the String :")
    Arr = input()

    Ret = CountCapital(Arr)

    print ("The Number of capital charracters in the string are :",Ret)
Main()
 