area=0
def Radius():
    global r
    r=int(input("Enter the radius:"))

def calcArea():
    global area
    area=(r**2)*3.14

Radius()
calcArea()
print("The area of your cirlce whose radius is", r," is",area)
