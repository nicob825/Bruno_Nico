count=int(input("Enter the number you want to count by:"))
end=int(input("Enter the number you want to count too:"))
output="    "
for i in range (count, end+1, count):
    output= output+str(i)+"    "
print(output)
