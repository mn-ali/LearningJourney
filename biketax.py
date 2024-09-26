a = int(input("Enter Ex-Showroom Price: "))
if a>100000:
    print("The tax to be paid is: ", (a/100)*15)
    print("Hence the total amount (On-Road Price): ", a+(a/100)*15)
if a>50000 and a<=100000:
    print("The tax to be paid is: ", (a/100)*10)
    print("Hence the total amount (On-Road Price): ", a+(a/100)*10)
if a<=50000:
    print("The tax to be paid is: ", (a/100)*5)
    print("Hence the total amount (On-Road Price): ", a+(a/100)*5)

