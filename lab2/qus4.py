import sys

dob = input("Enter the date of birth in the format dd/mm/yyyy: ")
dob_day, dob_month, dob_year = map(int, dob.split('/'))

if dob_month == 1 or dob_month == 3 or dob_month == 5 or dob_month == 7 or dob_month == 8 or dob_month == 10 or dob_month == 12:
    if dob_day <= 31:
        print("Input is valid")
    else:
        sys.exit("the input is invalid")
elif dob_month == 4 or dob_month == 6 or dob_month == 9 or dob_month == 11:
    if dob_day <= 30:
        print("Input is valid")
    else:
        sys.exit("the input is invalid")
elif dob_month == 2:
    if (dob_year % 4 == 0 and dob_year % 100 != 0) or dob_year % 400 == 0:
        print("The year is a leap year")
        if dob_day <= 29:
            print("Input is valid")
        else:
            sys.exit("the input is invalid")
    else:
        if dob_day >= 28:
            print("Input is valid")
        else:
            sys.exit("the input is invalid")


current_date = input("Enter the current date in the format dd/mm/yyyy: ")
current_day, current_month, current_year = map(int, current_date.split('/'))

if current_month == 1 or current_month == 3 or current_month == 5 or current_month == 7 or current_month == 8 or current_month == 10 or current_month == 12:
    if current_day <= 31:
        print("Input is valid")
    else:
        sys.exit(" the input is invalid")
elif current_month == 4 or current_month == 6 or current_month == 9 or current_month == 11:
    if current_day <= 30:
        print("Input is valid")
    else:
        sys.exit("the input is invalid")
elif current_month == 2:
    if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
        print("The year is a leap year")
        if current_day <= 29:
            print("Input is valid")
        else:
            sys.exit("the input is invalid")
    else:
        if current_day <= 28:
            print("Input is valid")
        else:
            sys.exit("the input is invalid")

age_in_days = (current_year - dob_year) * 365 + (current_month - dob_month) * 30 + current_day - dob_day

print("Age in Days:", age_in_days)