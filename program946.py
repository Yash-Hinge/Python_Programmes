
def DisplayFactors(No):
    
    for i in range(1,int((No/2)+1)):
        if (No%i==0):
            print(i)
        



def Main(): 
    Value=0
    print("Enter The Number :")
    Value = int(input()) 
    DisplayFactors(Value)

Main()
