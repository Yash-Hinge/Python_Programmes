import Marvellous as MI     #MI is alias name for Marvellous.'as' indicates the same 

def main():
    print("Enter the First Number :")
    iValue1=int(input()) 

    print("Enter the Second Number :")
    iValue2=int(input())
    ret = MI.Addition(iValue1,iValue2)     
    print(ret)



if(__name__)=="__main__":
    main()


