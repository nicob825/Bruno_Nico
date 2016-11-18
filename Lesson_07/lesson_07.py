number=int(input("Enter your number:"))
digit=0
num=number
while  num > 0:
    digit += 1
    num = int(num / 10)
print("There are ",digit," digits in", number)
    
