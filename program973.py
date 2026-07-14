
def lowerCase(Brr):
    Result = ""
    for ch in Brr:
        if(ch>='A' and ch<='Z'):
            Result = Result +chr(ord(ch)+32)
           
        else:
            Result = Result +ch

    return Result

def Main(): 
    print("Enter the String :")
    Arr = input()


    Ret = lowerCase(Arr)
    print("Updated String is : ",Ret )
         
Main()
 