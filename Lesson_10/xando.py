xsandos = []
import random
for i in range(0, 4):
    xsandos.append([])
    for j in range(0, 4):
        switch = random.randint(0, 2)
        if switch == 1:
            xsandos[i].append("X")
        else:
            xsandos[i].append("O")
for values in xsandos:
    output = ""
    for value in values:
        output += value
    print(output)
