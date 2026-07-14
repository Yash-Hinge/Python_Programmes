def Area(Radius,PI):
    Area = PI*(Radius*Radius)
    return Area

def main():
    Ret =Area(10.5,3.1428)
    print("The Area of Circle is :",Ret,"sq.cm")

    Ret =Area(13.6,7.12)
    print("The Area of Circle is :",Ret,"sq.cm")

if (__name__)=="__main__":
    main()