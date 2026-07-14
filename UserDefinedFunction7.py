def Calculation(No1,No2):
   Sum =No1+No2
   Diff =No1-No2
   Mult = No1*No2
   Div = No1/No2
   return Sum,Diff,Mult,Div
   


def main():
    
    Value1 = int(input("Enter the First number:"))
    Value2 = int(input("Enter the Second number:"))
    Ret1,Ret2,Ret3,Ret4 = Calculation(Value1,Value2)


    print("The Sum is :",Ret1)
    print("The Difference is :",Ret2)
    print("The multipication is :",Ret3)
    print("The Division is :",Ret4)




if(__name__)=="__main__":
  main()
 