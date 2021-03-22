n= int(input("Emter the year"))
if n%4== 0:
    if n%100== 0:
        if n%400== 0:
            print("{n} is a leap year", format(n))
        else:
            print("{n} is not a leap year", format(n))
    else:
       print("{n} is a leap year", format(n))
else:
    print("{n} is not a leap year", format(n))
