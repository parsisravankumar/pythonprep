"""17.Rajesh’s basic salary is input through the keyboard. His D.A. is 40% of basic
salary, and H.R.A. is 20% of basic salary. Write a program to calculate his
gross salary"""
basic_salary = float(input("enter the salary:"))
da = 0.4 * basic_salary
hra = 0.2 * basic_salary
gross_salary = basic_salary+da+hra
print("rajesh gross salary is rs:", gross_salary)
