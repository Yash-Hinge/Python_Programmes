class ArrayX():
    def __init__(self,size):
        self.size =size
        self.Arr=[0]*size
    
    def Accept(self):
        print("Enter Elements :")

        for i in range(self.size):
            Value = int(input())
            self.Arr[i] = Value

    def Display(self):
        print(" Elements of the Array are :")

        for i in range(self.size):
            print(self.Arr[i])

    def Summation(self):
        iSum =0
        for i in range(self.size):
            iSum = iSum+self.Arr[i]

        return iSum



def main():
    aobj = ArrayX(5)
    aobj.Accept()
    aobj.Display()

    ret = aobj.Summation()

    print("Summation is :",ret)

if __name__ =="__main__":
    main()