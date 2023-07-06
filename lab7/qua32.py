"""32. Write a program to read three sides a, b, c of a triangle and print the type of 
the triangle."""
a = int(input("enter the value of side a"))
b = int(input("enter the value of side b"))
c = int(input("enter the value of side c"))
s = (a + b + c)/2
area = s* (s-a)* (s-b)* (s-c)* .05
if a == b == c:
    print("the given triangle is a equalateral triangle")
elif a == b or b == c or c == a:
    print("the given triangle is a isoceles triangle")
else:
    print("the given triangle is a scalane triangle")