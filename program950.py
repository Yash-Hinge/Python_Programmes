
def SumDigits(No):
    DigitSum =0


    while No!=0:
        DigitSum = DigitSum +int(No%10) #if not tyoecasted to int will increase the iterations as treated as float.
        No = int(No/10)                 #Alternate Solution is using //(floar division) operator - it removes the decimal part


    return DigitSum

def Main(): 

    Value =0
    print("Enter the number :")
    Value =int(input())

    iRet =SumDigits(Value)

    print("The Sum of Digits of the Number is :",iRet)
Main()
 