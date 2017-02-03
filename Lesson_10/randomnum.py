
nums = []
import random
for i in range(0, 4):
    nums.append([])
    for j in range(0, 4):
        nums[i].append(random.randint(1, 100))


for numbers in nums:
    output = ""
    for number in numbers:
        output += str(number) + " "
    print(output)
