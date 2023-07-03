principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the interest rate:"))
time = float(input("Enter the time period in years:"))
simple_intrest = principal*rate*time/100
compound_intrest = principal * (1 + rate / 100) ** time
print("simple intrest for given principal is:",simple_intrest)
print("compond intrest for given principal is:",compound_intrest)
