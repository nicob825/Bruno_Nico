
def passCheck():
    username=input("Please enter your username:")
    password=input("Please enter your password:")

    if username=="Hello" and password=="Why":
        print("You are granted access!")
    
    else:
        if username=="Hello":
            print("Your password is incorrect.")
            passCheck()
        elif password=="Why":
            print("Your username is incorrect.")
            passCheck()
        else:
            print("Your username and password is incorrect.")
            passCheck()
            
passCheck()
