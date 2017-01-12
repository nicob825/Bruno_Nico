wor=input("Please enter a word:")
def tree(word):
    for x in range(1,len(word)+1):
        print("{:>20}".format(word[0:x]))

tree(wor)
