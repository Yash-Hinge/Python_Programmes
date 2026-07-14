
def main():
    ans =0
    try:
        print("Enter First Number :")
        no1 = int(input())

        print("Enter Second Number :")
        no2 = int(input())

        ans = no1/no2
        print("Division is successful")

    except Exception as eobj :
        print ( "Exception occured ",eobj)


    
    
    
    print("result is : ",ans)




if __name__ == "__main__":
    main()