class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B


    

    #Ret = Addition(Aobj,Value1,Value2)
    def Addition(self):      #issue

        Ans = self.No1+self.No2
        return Ans 


    def Subtraction(self):   #error       

        Ans = self.No1-self.No2
        return Ans 
    

  


print("Enter The First Number:")
No1 = int(input())
print("Enter The Second Number:")
No2 = int(input())
Aobj = Arithematic(No1,No2)
ret = Aobj.Addition()
print("The addition is :",ret)

ret = Aobj.Subtraction()
print("The Subtraction is :",ret )