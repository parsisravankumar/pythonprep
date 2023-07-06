# 31. Write a program to read ten numbers and print their sum by using ‘if’ statement.
sum = 0
for i in range(10):
    num = int(input("Enter a number:"))
    if num > 0:
     sum += num
print("The sum of positive numbers is:", sum)