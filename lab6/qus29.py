"""29. Write a program to find the roots of a given quadratic equation and print the
nature of roots."""
numbers = []

while True:
    num = int(input("Enter a positive number (or a negative number to exit): "))

    if num < 0:
        break

    numbers.append(num)

print("Positive numbers entered:", numbers)