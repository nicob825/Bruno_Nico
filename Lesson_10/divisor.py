nums = []


import random
for i in range(0, 4):
    nums.append([])
    for j in range(0, 4):
        nums[i].append(random.randint(0, 100))

for numbers in nums:
    output = ""
    for number in numbers:
        output += str(number) + " "
    print(output)

division=int(input("Enter a number for division:"))
count=0


for numbers in nums:
    for number in numbers:
        if number % division == 0:
             count += 1

print("There are",count,"numbers divisible by",division,"in the list.")
