class Demo :
    def __init__(self,A,B):
        print("Inside Constructor ")
        self.No1 = A
        self.No2 = B


    def Display(self):
        print("Inside Display")





def Main(): 

    obj1 = Demo(11,22)
    obj2 = Demo(10,20)

    print(obj1.No1)
    print(obj2.No2) 

    obj1.Display()
    obj2.Display()        
Main()
 