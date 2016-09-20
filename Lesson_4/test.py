def format(item,price):
    print("{:.<10}\t{:10.2f}".format(item,price))

#input item1
item1=input("Please enter item1:")
price1=float(input("please enter the price:"))
#input item2
item2=input("Please enter item2:")
price2=float(input("please enter the price:"))
#input item3
item3=input("Please enter item3:")
price3=float(input("please enter the price:"))
#calculate subtotal
subtotal=price1+price2+price3
tax=0.08*subtotal
total=subtotal*tax
print("<<<<<recipt>>>>>>")
format(item1,price1)
format(item2,price2)
format(item3,price3)
format("Subtotal:",subtotal)
format("tax",tax)
#same thing for tax, and total
print("_______________________________________")
#print "thank you" message here
