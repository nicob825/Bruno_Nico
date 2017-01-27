import random

numbers = []
for i in range(0, 10):
    numbers.append(random.randint (1, 100))
print("Numbers...")

output = ""
for number in numbers:
    output += str(number) + " " 
print(output)
print(" ")


def average():
    avg = 0
    for number in numbers:
        avg += number
    avg /= len(numbers)
    return avg
        
print("The average of the above numbers is...", average())
