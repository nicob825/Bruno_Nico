number=int(input("Enter a number:"))
numb=number
def Luck(num):
    if num > 0:
        if num % 10 == 7:
            return 1 + Luck(int(num/10))
        else:
            return 0 + Luck(int(num/10))
    return 0
print(Luck(numb))


