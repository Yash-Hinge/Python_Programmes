from functools import reduce

def Checkeven(No):
    return(No%2==0)


def Increment(no):
    no = no+1
    return no

def Summation(No1,No2):
   
    return No1+No2

def main():
    Data =[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData = list(filter(Checkeven,Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment,FData))
    print("Data after Filter :",MData)

    RData = reduce(Summation,RData)
    print("The Data from Reduce is :",RData)



if(__name__)=="__main__":
    main()