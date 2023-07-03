"""Write a program to read the marks of 3 subjects and display the total, average,
class."""
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

total_marks = sub1 + sub2 + sub3

average_marks = (sub1 + sub2 + sub3)/3

# Determine class based on average marks
if average_marks >= 90:
    class_name = "Excellent"
elif average_marks >= 80:
    class_name = "very good"
elif average_marks >= 70:
    class_name = "good"
elif average_marks >= 60:
    class_name = "satisfactory"
else:
    class_name = "below average"

print("total marks:", total_marks)
print("average :", average_marks )
print("class :",class_name)

