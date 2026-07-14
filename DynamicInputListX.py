def Sum(Marks):
    Sum =0
    for No in Marks :
        Sum =Sum + No

    return Sum


def main():
    Marks = list()

    print("enter the no . of marks : ")
    Size = int(input())
    no =0

    print("Enter the elemnts :")
    for i in range(Size):
        no = int(input())
        Marks.append(no) 

    print("The Entered marks are ",Marks)
    
    Ret = Sum(Marks)
    print("the addition of Given marks is :",Ret)


if(__name__)=="__main__":
    main()
