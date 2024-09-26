a = int(input("Enter the number of units: "))
b = 0
if a<=100:
    b = 0
if a>100 and a<=200:
    b = (a-100)*5
    print("Total Bill: ", b)
if a>200:
    b = 500+(a-200)*10
    print("Total Bill: ", b)
