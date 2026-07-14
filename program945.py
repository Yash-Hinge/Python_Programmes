
def CheckEven(No):
    
        if(No%2==0):
            print("it is an Even Number.")
        
        else:
             print("it is a Odd Number")


def Main(): 
    Value=0
    print("Enter The Number :")
    Value = int(input()) 
    CheckEven(Value)

Main()
