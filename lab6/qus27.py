#27. Write a program to find biggest of given three numbers
num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
num3 = int(input("enter the number:"))
if num1 > num2 and num1 > num3:
    print("the biggest of given three numbers is :", num1)
elif num2 > num3 and num2 > num1:
    print("the biggest of given three numbers is :", num2)
else:
    print("the biggest of given three numbers is :", num3)