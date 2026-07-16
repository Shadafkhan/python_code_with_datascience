'''20. ⭐ Ultimate Challenge – College ERP Mini System

Take all the following:

Student Name
Roll Number
Course
Semester
Tuition Fee
Exam Fee
Library Fee
Hostel Fee
Bus Fee
Scholarship %
Marks of 6 Subjects

Generate one complete report containing:

Section 1

Student Profile

Section 2

Fee Receipt

Total Fee
Scholarship
Final Fee
Section 3

Academic Report

Total Marks
Average
Percentage
Section 4

Student Summary

Name
Course
Semester
Final Fee
Percentage'''

student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
course = input("Enter Course: ")
semester = input("Enter Semester: ")

tuition_fee = float(input("Enter Tuition Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
library_fee = float(input("Enter Library Fee: "))
hostel_fee = float(input("Enter Hostel Fee: "))
bus_fee = float(input("Enter Bus Fee: "))
scholarship = float(input("Enter Scholarship (%): "))

print("\nEnter Marks of 6 Subjects")

sub1 = float(input("Enter marks of Maths: "))
sub2 = float(input("Enter marks of English: "))
sub3 = float(input("Enter marks of Computer Fundamnetal: "))
sub4 = float(input("Enter marks of Python : "))
sub5 = float(input("Enter marks of DSA 5: "))
sub6 = float(input("Enter marks of C : "))

# ---------------- Fee Calculation ----------------

total_fee = tuition_fee + exam_fee + library_fee + hostel_fee + bus_fee
scholarship_amount = total_fee * scholarship / 100
final_fee = total_fee - scholarship_amount

# ---------------- Marks Calculation ----------------

total_marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
average = total_marks / 6
percentage = (total_marks / 600) * 100

# ---------------- Report ----------------

print(f"\n{40*"="}")
print("       COLLEGE ERP MINI SYSTEM")
print(f"\n{40*"="}")

print("\n----------- SECTION 1 -----------")
print("Student Profile")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Course       :", course)
print("Semester     :", semester)

print("\n----------- SECTION 2 -----------")
print("Fee Receipt")
print("Total Fee           :", total_fee)
print("Scholarship Amount  :", scholarship_amount)
print("Final Fee           :", final_fee)

print("\n----------- SECTION 3 -----------")
print("Academic Report")
print("Total Marks :", total_marks)
print("Average     :", average)
print("Percentage  :", percentage, "%")

print("\n----------- SECTION 4 -----------")
print("Student Summary")
print("Name        :", student_name)
print("Course      :", course)
print("Semester    :", semester)
print("Final Fee   :", final_fee)
print("Percentage  :", percentage, "%")

print(f"\n{40*"="}")
print("        THANK YOU")
print(f"\n{40*"="}")