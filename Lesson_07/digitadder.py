def sumDigit():
    global num
    global summ
    while num > 0:
        summ += num % 10 
        num = int(num / 10)

number=int(input("Enter the number:"))
num=number
summ = 0

sumDigit()

print("The sum of the digits in",number," is",summ)
