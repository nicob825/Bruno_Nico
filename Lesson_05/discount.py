def formater(item1,item2,item3,item4,price1,price2,price3,price4,subtotal,total):
    print("{
    print("{:<12}{:<12}".format(item1, price1))
    print("{:<12}{:<12}".format(item2, price2))
    print("{:<12}{:<12}".format(item3, price3))
    print("{:<12}{:<12}".format(item4, price4))
    print("{:<12}".format(subtotal))
    print("{:<12}".format(total))
    print("_"*36)
    print("{:12}







item1=input("Please enter the item you are buying:")
item2=input("Please enter the item you are buying:")
item3=input("Please enter the item you are buying:")
item4=input("Please enter the item you are buying:")
price1=int(input("Please enter the price of item 1:"))
price2=int(input("Please enter the price of item 2:"))
price3=int(input("Please enter the price of item 3:"))
price4=int(input("Please enter the price of item 4:"))

subtotal=(price1+price2+price3+price4)
discount=subtotal*0.15
total=(subtotal-discount)*0.08



