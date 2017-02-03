def circle():
    global r, area
    r=float(input("Enter the radius of the cirlce:"))
    area=(r**2)*3.14
def calcCircle():
    print("The area of the cirlce whoes radius is",r,"is",area)
circle()
calcCircle()
