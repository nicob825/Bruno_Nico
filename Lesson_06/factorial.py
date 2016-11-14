number=int(input("Please enter the number:"))
factorial=1
for i in range (0, number):
    factorial *= (number - i)
print(factorial)
    
