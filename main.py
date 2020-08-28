

def fiz_buz():
    value = None 
    value = int(input("Please Enter The Desired Number : "))
    print(f"You have Entered {value}")


    if value % 3 == 0 and value % 5 == 0:
        print("Your Entered Number is Divisible by both 3 & 5 : BUZZZ-FIZZZ")        
        
    elif value % 3 == 0:
        print("Your Entered Number is Divisible by 3 : BUZZZ")
        
    elif value % 5 == 0:
        print("Your Entered Number is Divisible by 5 : FIZZZ")             

    else:
        print("Sorry the Number is Neither Divisible by 3 or 5")
        
fiz_buz()