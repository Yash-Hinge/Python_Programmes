
class node:
    def __init__(self,Value):
        self.data =Value
        self.next =None

class SinglyLL:
    def __init__(self):
        self.first =None
        self.iCount=0

    def InsertFirst(self,No):
        temp = self.first
        nobj = node(No)
        
        if(self.first is None):
            self.first =nobj
            nobj.next =None
            
            

        elif(self.first is not None):
            nobj.next = self.first
            self.first =nobj 

        self.iCount =self.iCount+1


    def InsertLast(self,No):
        temp = self.first
        nobj = node(No)
        if(temp is None):
            self.InsertFirst(No)
            

        elif(temp is not None):
            while temp.next is not None:
                temp=temp.next

            temp.next =nobj
            nobj.next=None

        self.iCount =self.iCount+1



        
    def InsertAtPos(self,Pos,No):
        temp = self.first
        nobj = node(No)
        iCnt =0
        if(Pos<1 or Pos>(self.iCount+1)):
            print("Invalid Position...")
            return 
        if(Pos == 1):
            self.InsertFirst(No)
            
            return
        
        elif(Pos == self.iCount+1):
            self.InsertLast(No)
            
            return
        elif(Pos>1 and Pos<self.iCount):
            for iCnt in range(1,(Pos-1)):
                temp = temp.next
                
            nobj.next =temp.next
            temp.next =nobj
            


        self.iCount =self.iCount+1
        
                


    def DeleteFirst(self):
        if(self.first ==None):
            return
        
        else:
            self.first = self.first.next

        self.iCount = self.iCount-1

    def DeleteLast(self):
        temp = self.first
        if(self.first.next ==None):
            del self.first
            self.first=None
        
        else :
            while temp.next.next is not None:
                    temp=temp.next

            del temp.next
            temp.next =None
            self.iCount = self.iCount-1

    def DeleteAtPos(self,Pos):
        temp = self.first
        if(Pos==1):
            self.DeleteFirst()

        elif(Pos==self.iCount):
            self.DeleteLast()

        else:
            for iCnt in range(1,(Pos-1)):
                temp = temp.next
                
            temp.next=temp.next.next

            self.iCount = self.iCount-1




    def CountElements(self):
        return self.iCount
    

    def display(self):
        temp =self.first
        while temp is not None :

            print(" | ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")

        print ("The No. of elements in the Linked list are :",self.iCount)
    


def main():
    Sobj = SinglyLL() 


    Sobj.InsertFirst(11)
    Sobj.InsertFirst(21)
    Sobj.InsertFirst(121)
    Sobj.display()
    Sobj.InsertLast(51)
    Sobj.InsertLast(111)
    Sobj.InsertLast(121)
    Sobj.display()
    Sobj.InsertAtPos(3,31)
    Sobj.display()

    Sobj.DeleteFirst()
    Sobj.display()

    Sobj.DeleteLast()
    Sobj.display()

    Sobj.DeleteAtPos(3)
    Sobj.display()

  
if  __name__ =="__main__" :
    main()