def Area(PI=3.14,Radius):       #Error:-Default arguments should be defined at the last 
    Area = PI*(Radius*Radius)
    return Area

def main():
    Ret =Area(Radius=10.5)
    print("The Area of Circle is :",Ret,"sq.cm")
    Ret =Area(Radius=10.5,PI=7.28)
    print("The Area of Circle is :",Ret,"sq.cm")



if (__name__)=="__main__":
    main()