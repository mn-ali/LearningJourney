a = int(input("Enter a number: "))
if(a%8==0 and a%9==0 and a%7==0 and a%5==0):
    print("This number is divisible by all numbers from 1-10")
elif(a%9==0 and a%8==0 and a%5==0):
    print("This number is divisible by 10, 9, 8, 6, 5, 4, 3 & 2")
elif(a%9==0 and a%4==0 and a%5==0):
    print("This number is divisible by 10, 9, 6, 5, 4, 3 & 2")
elif(a%8==0 and a%5==0 and a%3==0):
    print("This number is divisible by 10, 8, 6, 5, 4, 3 & 2")
elif(a%8==0 and a%5==0 and a%3==0):
    print("This number is divisible by 10, 9, 6, 5, 4, 3 & 2")
elif(a%9==0 and a%5==0 and a%2==0):
    print("This number is divisible by 10, 9, 6, 5, 3 & 2")
elif(a%8==0 and a%7==0 and a%5==0):
    print("This number is divisible by 10, 8, 7, 5, 4 & 2")
elif(a%7==0 and a%6==0 and a%5==0):
    print("This number is divisible by 10, 7, 6, 5, 3 & 2")
elif(a%5==0 and a%4==0 and a%3==0):
    print("This number is divisible by 10, 6, 5, 4, 3 & 2")
elif(a%9==0 and a%7==0 and a%4==0):
    print("This number is divisible by 9, 7, 6, 4, 3 & 2")
elif(a%8==0 and a%7==0 and a%3==0):
    print("This number is divisible by 8, 7, 6, 4, 3 & 2")
elif(a%7==0 and a%5==0 and a%4==0):
    print("This number is divisible by 10, 7, 5, 4 & 2")
elif(a%9==0 and a%7==0 and a%2==0):
    print("This number is divisible by 9, 7, 6, 3 & 2")
elif(a%7==0 and a%4==0 and a%3==0):
    print("This number is divisible by 7, 6, 4, 3 & 2")
elif(a%7==0 and a%5==0 and a%2==0):
    print("This number is divisible by 10, 7, 5 & 2")
elif(a%9==0 and a%7==0 and a%5==0):
    print("This number is divisible by 9, 7, 5 & 3")
elif(a%7==0 and a%5==0 and a%3==0):
    print("This number is divisible by 7, 5 & 3")
elif(a%9==0 and a%8==0):
    print("This number is divisible by 9, 8, 6, 4, 3 & 2")
elif(a%8==0 and a%5==0):
    print("This number is divisible by 10, 8, 5, 4 & 2")
elif(a%9==0 and a%4==0):
    print("This number is divisible by 9, 6, 4, 3 & 2")
elif(a%8==0 and a%6==0):
    print("This number is divisible by 8, 6, 4, 3 & 2")
elif(a%6==0 and a%5==0):
    print("This number is divisible by 10, 6, 5, & 2")
elif(a%5==0 and a%4==0):
    print("This number is divisible by 10, 5, 4 & 2")
elif(a%9==0 and a%6==0):
    print("This number is divisible by 9, 6, 3 & 2")
elif(a%8==0 and a%7==0):
    print("This number is divisible by 8, 7, 4 & 2")
elif(a%7==0 and a%6==0):
    print("This number is divisible by 7, 6, 3 & 2")
elif(a%6==0 and a%4==0):
    print("This number is divisible by 6, 4, 3 & 2")
elif(a%9==0 and a%7==0):
    print("This number is divisible by 9, 7, & 3")
elif(a%9==0 and a%5==0):
    print("This number is divisible by 9, 5, & 3")
elif(a%7==0 and a%4==0):
    print("This number is divisible by 7, 4, & 2")
elif(a%5==0 and a%2==0):
    print("This number is divisible by 10, 5, & 2")
elif(a%3==0 and a%2==0):
    print("This number is divisible by 6, 3, & 2")
elif(a%7==0 and a%5==0):
    print("This number is divisible by 7, & 5")
elif(a%7==0 and a%3==0):
    print("This number is divisible by 7, & 3")
elif(a%7==0 and a%2==0):
    print("This number is divisible by 7, & 2")
elif(a%5==0 and a%3==0):
    print("This number is divisible by 5, & 3")
elif(a%9==0):
    print("This number is divisible by 9, & 3")
elif(a%8==0):
    print("This number is divisible by 8, 4 & 2")
elif(a%6==0):
    print("This number is divisible by 6, 3 & 2")
elif(a%4==0):
    print("This number is divisible by 4, & 2")
elif(a==7):
    print("This number is a Prime!!")
elif(a==5):
    print("This number is a Prime!!")
elif(a==3):
    print("This number is a Prime!!")
elif(a==2):
    print("This number is a Prime!!")
elif(a%7==0):
    print("This number is divisible by 7, & ", a/7)
elif(a%5==0):
    print("This number is divisible by 5, & ", a/5)
elif(a%3==0):
    print("This number is divisible by 3, & ", a/3)
elif(a%2==0):
    print("This number is divisible by 2, & ", a/2)
else:
    print("This number may be a Prime (Algorihtm has divisibility rules only for 1 - 10. Numbers such as 121, 169 are not primes but the output is this)")

