# Write a program to print the area of a triangle if three sides are given
import math
a = float(input("enter the value:"))
b = float(input("enter the value:"))
c = float(input("enter the value:"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("area of a triangle if three sides are given is :", area)
