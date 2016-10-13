one=int(input("please enter number"))
two=int(input("please enter a second number:"))
even=(one+two)%2==0
if even:
    print((one+two),"is even!")
if not even:
    print((one+two),"is odd!")
