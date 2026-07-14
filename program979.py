
class Arithematics :
    def __init__(self,A,B):
        self.no1 =A
        self.no2 = B

    def Addition(self):

        self.Result = self.no1+self.no2
        return self.Result

    def Subtraction(self):

        self.Result = self.no1-self.no2
        return self.Result


def Main(): 
       
    Value1 =0
    Value2 =0

    print("Enter the First Number")
    Value1 = int(input())

    print("Enter the Second Number")
    Value2 = int(input())

    Aobj = Arithematics(Value1,Value2)

    Ret = Aobj.Addition()
    print("Addition is ",Ret)

    Ret = Aobj.Subtraction()
    print ("Subtraction is",Ret)



Main()
 