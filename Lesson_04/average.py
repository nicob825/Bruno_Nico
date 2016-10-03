def avg():
    global num1, num2, num3, avg
    num1=float(input("Enter number 1:"))
    num2=float(input("Enter number 2:"))
    num3=float(input("Enter number 3:"))
    avg="{:0.5f}".format((num1+num2+num3)/3)

def calcAvg():
    print("The average of these numbers is",avg)


avg()
calcAvg()
