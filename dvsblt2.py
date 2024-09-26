while True:
    a = int(input("Enter a number: "))
    b = 1
    while b<=a:
        b = b + 1
        if(a%b==0):
            print(a, "is divisible by", b)
