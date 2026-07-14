

Checkeven= lambda No:No%2==0


Increment = lambda NO :NO+1


Summation = lambda No1,No2:No1+No2
   
def filterX(Func_name,data):
    Result=list()
    for i in data:
       Ret = Func_name(i)
       if(Ret==True):
        Result.append(i)

    return Result


def MapX(Func_name,Elements):
    result = list()
    for i in Elements :
      Ret = Func_name(i)
      result.append(Ret)
    
    return result

def ReduceX(Func_name,Elements):
   
    value1=0

    for i in Elements :
      
      value1 = Func_name(i,value1)
      
    return value1

      

def main():
    Data =[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData = list(filterX(Checkeven,Data))
    print("Data after Filter :",FData)

    MData = list(MapX(Increment,FData))
    print("Data after map :",MData)

    RData = ReduceX(Summation,MData)
    print("The Data from Reduce is :",RData)



if(__name__)=="__main__":
    main()