def calcPayment(r, P, n, t):
    return P*((1+r/n)**(n*t))/(t*12)

r=float(input("Enter the interest rate:"))
P=float(input("Enter the principal:"))
n=float(input("Enter the number of times the loan is compunded per year:"))
t=float(input("Enter the life of the loan in years:"))

print("The interest of your loan is {:0.2f}".format(calcPayment(r, P, n, t))
      

