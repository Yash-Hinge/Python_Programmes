class Arithematic:

    def __init__(self,No1,No2):
        self.No1 =No1
        self.No2 =No2


    def Addition(No1,No2):      #issue

        Ans = No1+No2
        return Ans 


    def Subtraction(No1,No2):   #error       

        Ans = No1-No2
        return Ans 
    




print("Enter The First Number:")
No1 = int(input())
print("Enter The Second Number:")
No2 = int(input())
Aobj = Arithematic(No1,No2)
ret = Aobj.Addition(No1,No2)
print("The addition is :",ret)

ret = Aobj.Subtraction(No1, No2)
print("The Subtraction is :",ret )