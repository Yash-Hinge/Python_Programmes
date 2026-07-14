from functools import reduce

Checkeven= lambda No:No%2==0


Increment = lambda NO :NO+1


Summation = lambda No1,No2:No1+No2
   

def main():
    Data =[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData = list(filter(Checkeven,Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment,FData))
    print("Data after Filter :",MData)

    RData = reduce(Summation,MData)
    print("The Data from Reduce is :",RData)



if(__name__)=="__main__":
    main()