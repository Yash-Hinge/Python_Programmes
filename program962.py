def Maximum(Brr):
    isum =0
    iMax = Brr[0]
    for i in range(len(Brr)) :
        if(Brr[i]>iMax):
            iMax = Brr[i]


    return iMax

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
       

    Ret = Maximum(Arr)

    print("Maximum is :",Ret)


    
        
Main()
 