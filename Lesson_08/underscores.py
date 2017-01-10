sentence=input("Please enter a sentence:")

def replace(sen):
    if " " not in sen:
        return sen
    else:
        return sen[0:sen.index(" ")] + "_" + replace(sen[sen.index(" ")+1:len(sen)])

print(replace(sentence))
