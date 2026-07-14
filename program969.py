def CountSmall(Brr):

    Cntlwr =0

    for i in range(len(Brr)):
         if(Brr[i]>'a' and Brr[i]<'z'):
             Cntlwr=Cntlwr+1

    return Cntlwr


def Main(): 
    print("Enter the String :")
    Arr = input()

    Ret = CountSmall(Arr)

    print ("The Number of capital charracters in the string are :",Ret)
Main()
 