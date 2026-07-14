def Summation(Brr):
    isum =0
    for no in Brr :
        isum = isum+no 

    return isum

def Main(): 
    size =0
    Arr =[]
    Value =0
    print("Enter the Size :")
    size = int(input())
    print("Enter the elements :")

    for i in range(0,size,1):
        Value = int(input())
        Arr.append(Value)
       

    Ret = Summation(Arr)

    print("Summmation is :",Ret)


    
        
Main()
 