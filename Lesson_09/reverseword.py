

myList = ["animal", "dog", "fish", "food", "game"]

print("In order...")
output = ""

for i in myList:

    output += i + " "

print(output)

print("")


print("Reversed...")
def wordReverse (array):
    for i in reversed(array):
        print (i,end=' ')


wordReverse(myList)
    


