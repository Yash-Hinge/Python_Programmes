def BigBazaar():
    print("Inside Big Bazaar")

    def Amul():
       print("Inside Amul Ice-Cream Parlour")
        
    


def main():

    BigBazaar()     #Allowed
    Amul()          #Error
    BigBazaar.Amul()#Error


if(__name__)=="__main__":
  main()
 