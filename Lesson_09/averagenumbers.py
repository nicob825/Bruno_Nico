import random

numbers = []
for i in range(0, 10):
    numbers.append(random.randit (1, 100))
print("Numbers...")

output = ""
for number in numbers:
    output += number + " " 
print(output)
print(" ")
print("The average of the above numbers is..." + avg)

def average():
      summ = 0
      for i in numbers:
          summ += i
      avg = summ/len(numbers)


average()
