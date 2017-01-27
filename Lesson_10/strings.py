go = input("Enter 16 stings:")
splitList = go.split(" ")
print(splitList)
wordList = []
spot = 0
for i in range (0, 4):
    output = ""
    wordList.append([])
    for j in range (0, 4):
        wordList[i].append(splitList[spot])
        output += "{:10}".format(wordList[i][j])
        spot += 1
    print(output)
