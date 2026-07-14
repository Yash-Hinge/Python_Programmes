class Demo :
    # Class Variables
    Value1 =10
    Value2 =20


    def __init__(self):
        self.No1 = 11
        self.No2 = 21 


# instance Method 
    def Fun(self):
        print("Inside instance method named as Fun")

        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def gun(cls):
            print("Inside class meyhod named as gun ")
           # print(Demo.No1)
            #print(Demo.No2)
            print(cls.Value1)
            print(cls.Value2)


    @staticmethod
    def sun():
        print("Inside Static method named as Sun")

        
        print(Demo.Value1)
        print(Demo.Value2)
         


Demo.sun()



