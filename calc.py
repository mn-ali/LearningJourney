# Exercise 1: Calculator using Python (calc.py)
import math

print("**Calculator**")
print("-For addition, enter \"+\" in Operation")
print("-For subtraction, enter \"-\" in Operation")
print("-For division, enter \"/\" in Operation")
print("-For multiplication, enter \"*\" in Operation")
print("-For power, enter \"**\" in Operation")
print("-For Floor Division (Returns integer part of the division), enter \"//\" in Operation")
print("-For Modulus (Returns remainder of the division), enter \"%\" in Operation")
print("-For \"log of first number to the base second number\", enter \"log\" in Operation")
print("-For \"(First Number)^(Second Number)\" enter \"pow\" in Operation")
print("-For Trigonometric Ratios (sin/cos/tan), enter sin/cos/tan in the first number, enter angle(in degrees) in the second number, enter \"NA\" in Operation")
while True:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    z = input("Operation: ")
    if x == "cos" and z == "NA":
        print(math.cos(math.radians(float(y))))
    if x == "sin" and z == "NA":
        print(math.sin(math.radians(float(y))))
    if x == "tan" and z == "NA":
        print(math.tan(math.radians(float(y))))
    if z == "+":
        print(float(x)+float(y))
    if z == "-":
        print(float(x)-float(y))
    if z == "*":
        print(float(x)*float(y))
    if z == "/":
        print(float(x)/float(y))
    if z == "%":
        print(float(x)%float(y))
    if z == "//":
        print(float(x)//float(y))
    if z == "**":
        print(float(x)**float(y))
    if z == "log":
        print(math.log(float(x), float(y)))
    if z == "pow":
        print(math.pow(float(x), float(y)))
