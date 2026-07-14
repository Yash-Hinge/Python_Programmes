from Marvellouslibrary import filterX,MapX,ReduceX

Checkeven= lambda No:No%2==0


Increment = lambda NO :NO+1


Summation = lambda No1,No2:No1+No2
   

      

def main():
    Data =[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData = list(filterX(Checkeven,Data))
    print("Data after Filter :",FData)

    MData = list(MapX(Increment,FData))
    print("Data after map :",MData)

    RData = ReduceX(Summation,MData)
    print("The Data from Reduce is :",RData)



if(__name__)=="__main__":
    main()