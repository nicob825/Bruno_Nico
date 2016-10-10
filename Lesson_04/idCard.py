def formater(firstname,lastname,title,year,subject,site):
    print("*"*26)
    print("*{:<12}{:<12}*".format(site, year))
    print("*{:<12}{:<12}*".format(firstname, lastname))
    print("*{:<12}{:<12}*".format(title, subject))
    print("*"*26)


firstname=input(format("Enter your first name:"))
lastname=input(format("Enter your last name:"))
title=input(format("Enter your title:"))
year=input(format("Enter your school year:"))
subject=input(format("Enter your school subject:"))
site=input(format("Enter your school site:"))
formater(firstname,lastname,title,year,subject,site)







