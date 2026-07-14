def addition(No1,No2):

    Ans = No1+No2
    return Ans 


def Subtraction(No1,No2):

    Ans = No1-No2
    return Ans 


def main():
    print("Enter The First Number:")
    No1 = int(input())
    print("Enter The Second Number:")
    No2 = int(input())

    ret = addition(No1,No2)
    print("The sum is :",ret)


    ret = Subtraction(No1,No2)
    print("The difference is :",ret)




if __name__ =="__main__":
    main()

