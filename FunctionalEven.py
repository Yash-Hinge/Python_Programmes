checkeven = lambda no  :(no%2==0)


def main():

    no = int(input("Enter the Number :"))
    Ret =checkeven(no)

    if(Ret==True):
        print("The entered number is even")

    else:
        print("The entered number id odd")



if(__name__)=="__main__":
    main()
