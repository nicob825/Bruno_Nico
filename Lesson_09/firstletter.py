myList = ["animal", "dog", "fish", "food", "game"]

print("The full words...")
output = ""

for i in myList:
    output += i + " "

print(output)

print("")

print("Just the first letters...")
def First():
    for i in myList:
        print(i[0])


First()
