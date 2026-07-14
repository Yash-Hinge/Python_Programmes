def Minimum(Brr):
    isum =0
    iMin = Brr[0]
    for i in range(len(Brr)) :
        if(Brr[i]<iMin):
            iMin = Brr[i]


    return iMin

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
       

    Ret = Minimum(Arr)

    print("Minimum is :",Ret)


    
        
Main()
 