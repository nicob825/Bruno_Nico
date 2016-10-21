def calcPoints(Grade):
    if Grade=="A":
        return 4.0
    elif Grade=="B":
        return 3.0
    elif Grade=="C":
        return 2.0
    elif Grade=="D":
        return 1.0
    else:
        return 0.0


Grade1=input("What is your grade in first period:")
Grade2=input("What is your grade in second period:")
Grade3=input("What is your grade in thrid period:")
Grade4=input("What is your grade in fourth period:")
Grade5=input("What is your grade in fifth period:")
Grade6=input("What is your grade in sixth period:")
Grade7=input("What is your grade in seventh period:")



GPA=(calcPoints(Grade1)+ calcPoints(Grade2)+ calcPoints(Grade3)+ calcPoints(Grade4)+ calcPoints(Grade5)+ calcPoints(Grade6)+ calcPoints(Grade7))/7

print("Your GPA is:",GPA)
