def calcVol(h,l,w):
    return (h*l*w)

h=float(input("Enter the height:"))
l=float(input("Enter the length:"))
w=float(input("Enter the width:"))

print("The cubic inches is {:0.2f} and the cubic feet is {:0.2f}".format(calcVol(h,l,w), calcVol(h,l,w)/1728))


