size=int(input("Enter size of graph:"))
integer=int(input("Enter the integer of the graph:"))
for i in range (0,size+1):
    print("{:5d} | {:5d}".format(i,i*integer))
