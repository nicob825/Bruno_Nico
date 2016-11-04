
perimiter=0
def Perim():
    global width, length
    length=int(input("Enter your length:"))
    width=int(input("Enter your width:"))

def calcPerim():
    global perimiter
    perimiter=(length*2)+(width*2)

Perim()
calcPerim()
print("The perimiter of your object is", perimiter)
    
