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
