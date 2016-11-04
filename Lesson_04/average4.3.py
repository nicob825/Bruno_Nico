avg=0
def AVG():
    global num1,num2,num3
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    num3=int(input("Enter the third number:"))

def calcAVG():
    global avg
    avg=(num1+num2+num3)/3

AVG()
calcAVG()
print("The numbers", num1,",",num2,"and",num3," are",avg)
