
def main():
    ans =0
    try:
        print("Enter First Number :")
        no1 = int(input())

        print("Enter Second Number :")
        no2 = int(input())

        ans = no1/no2
        print("Division is successful")
    except ZeroDivisionError as zobj :
        print("Exception Occured due to second operand is zero .:",zobj)

    except ValueError as vobj :
        print("Invalid character entered please enter numeric values only ")
    
    except Exception as eobj :
        print ( "Exception occured ",eobj)
    
    
    finally:
        print("inside finally block.")




if __name__ == "__main__":
    main()