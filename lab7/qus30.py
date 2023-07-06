""" 30.Write a program to read positive numbers continuously until negative number 
is given by using ‘if’."""
positive_numbers = []

while True:
    num = int(input("Enter a positive number (or a negative number to exit): "))
    
    if num < 0:
        break
    
    positive_numbers.append(num)

print("Positive numbers entered:")
print(positive_numbers)
