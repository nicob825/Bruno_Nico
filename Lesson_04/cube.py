def surfArea():
    global side, SA
    side=float(input("Enter the perimiter of the side:"))
    SA="{:0.5f}".format(side*6)
def calcSA():
    print("The surface area of the cube whoes sides are",side,"in perimiter is",SA)
surfArea()
calcSA()
