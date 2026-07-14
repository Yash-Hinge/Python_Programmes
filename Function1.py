def Addition(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    print("Enter the First Number :")
    iValue1=int(input()) 

    print("Enter the Second Number :")
    iValue2=int(input())

    ret = Addition(iValue1,iValue2)
    print(ret)



if(__name__)=="__main__":
    main()


