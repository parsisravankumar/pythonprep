"""33. Write a program to calculate the monthly income of a person using the 
following commission schedule:
Page 3 of 13
Monthly sales income
>= Rs.50,000 Rs.375 + 16% sales.
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
<= Rs.10,000 Rs. 200+3% sales"""
sales = float(input("enter the amount:"))
if sales >= 50000:
    income = 375 + (0.16 * sales)
elif sales >= 40000 and sales <= 50000:
   income = 350 + (0.14* sales)
elif sales >= 30000 and sales <= 40000:
    income = 325 + (0.12 * sales)
elif sales >= 20000 and sales <= 30000:
    income = 300 + (0.09 * sales)
elif sales >= 10000 and sales >= 20000:
    income = 250 + (0.5 * sales)
else:
    income = 200 + (0.03 * sales)
print("the montly income of a person is:", income)