#28. Write a program to check whether the given year is leap year or not.
year = int(input("enter the year:"))
if year % 4 == 0:
    print("the given year is a leap year")
else:
    print("the given year is a non leap year")