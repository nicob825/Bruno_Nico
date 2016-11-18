number=int(input("Enter the number:"))
num=number
sum=0
while num > 0:
    sum += 1
    num = int(num / 10)
print("The sum of the digits in",number," is",sum)
