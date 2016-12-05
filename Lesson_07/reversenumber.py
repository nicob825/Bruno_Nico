

def getReverse():
    global num, rev
    while num > 0:
        rev *= 10
        rev += num % 10
        num = int(num/10)
        

number=int(input("Enter the number:"))
rev = 0
num = number

getReverse()
print(number, "reversed is",rev)
