length=float(input("Enter the length of the object:"))
height=float(input("Enter the height of the object:"))
width=float(input("Enter the width of the object:"))
perimiter1=length*2+width*2
perimiter2=height*2+width*2
perimiter3=length*2+height*2
volume=width*height*length
SA=2*(length*width+length*height+width*height)
print("The perimiter of the sides of the rectangle are", perimiter1,perimiter2,perimiter3,"the volume of the object is",volume,"and the surface are is",SA)
