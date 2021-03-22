a= int(input("enter thye number"))
i=2
while i<a:
    if a%i == 0:
        print("Not prime")
        break
    i= i+1
else:
    print("prime")
