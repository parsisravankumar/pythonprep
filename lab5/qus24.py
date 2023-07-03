#24. Write a program to check whether the given number is positive or negative.
n = int(input("enter the number:"))
if n > 0:
    n = "positive"
elif n == 0:
    n = "neutral"
else:
    n = "negative"
print("given number is:",n)


