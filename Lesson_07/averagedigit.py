def avDigits():
    global num
    global average
    digits = len(str(number))
    while num > 0:
        average += num % 10
        num = int(num / 10)
    average = average/digits
        
average=0
number=int(input("Enter the number you want:"))
num=number
avDigits()
print("The average of the digits in",number," is",average)
