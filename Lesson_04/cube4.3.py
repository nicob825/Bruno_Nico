SA=0
def Cube():
    global side
    side=int(input("Enter your side length:"))

def calcSA():
    global SA
    SA=6*(side**2)

Cube()
calcSA()

print("The surface area of your cube is", SA," and the side is", side)
    
