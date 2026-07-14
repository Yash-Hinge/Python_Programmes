
def CheckPerfect(No):
    FactSum=0
    for i in range(1,int((No/2)+1)):
        if (No%i==0):
            FactSum =FactSum+i
            
    
    return [FactSum==No]


def Main(): 
    Value=0
    print("Enter The Number :")
    Value = int(input()) 
    iRet =CheckPerfect(Value)

    if(iRet ==True):
        print("It is a perfect Number.")
    
    else:
        print("It is not a perfect Number.")
    

Main()
