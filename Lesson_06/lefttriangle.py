word=input("Enter the word:")
def printRTri():
    for i in range(len(word),-1,-1):
        print(word[i:len(word)])

printRTri()
