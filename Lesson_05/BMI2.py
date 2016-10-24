weight=int(input("Enter your weight:"))
height=int(input("Enter your height in inches:"))
bmi=0

def calcBMI(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return "Normal"
    elif BMI < 30:
        return "Overweight"
    elif BMI < 35:
        return "Obese"
    elif BMI < 40:
        return "Very Obese"
    else:
        return "Morbidly Obese"


BMI=(703*weight)/(height**2)

print("Your BMI is:",BMI)
print("Your condition is:", calcBMI(BMI))
