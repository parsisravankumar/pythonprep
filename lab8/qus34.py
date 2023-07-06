"""34. Write a program to read a 3-digit number and find whether the middle digit is 
numerically equal to the sum of the other two digits and prints an appropriate 
response."""
num = int(input("enter a 3 digit number:"))
digit_one = num // 100
digit_two = (num // 10) % 10
digit_three = num %10
if digit_two == digit_one + digit_three:
    print("The middle digit is equal to the sum of the other two digits.")
else:
    print("The middle digit is not equal to the sum of the other two digits.")

