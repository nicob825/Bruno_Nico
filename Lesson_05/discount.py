def format(item,price):
    print("{:<10}........{:10.2f}".format(item,price))

def calcDisc(subtotal):
    if subtotal >= 2000:
        return 0.15 * subtotal
    if not total >= 2000:
        return 0.0

item1=input("Please enter the item you are buying:")
item2=input("Please enter the item you are buying:")
item3=input("Please enter the item you are buying:")
item4=input("Please enter the item you are buying:")
price1=int(input("Please enter the price of item 1:"))
price2=int(input("Please enter the price of item 2:"))
price3=int(input("Please enter the price of item 3:"))
price4=int(input("Please enter the price of item 4:"))

subtotal=(price1+price2+price3+price4)
discount = calcDisc(subtotal)
tax= 0.08 * subtotal
total=subtotal+tax-discount


print("<<<<<<<<<<Recipt>>>>>>>>>>>")
format(item1,price1)
format(item2,price2)
format(item3,price3)
format(item4,price4)
format("Subtotal:",subtotal)
format("Total:",total)
print("_"*28)
print("Thank you!")


