'''1. University Fee Management System

Take:

Student Name
Course
Tuition Fee
Exam Fee
Library Fee
Hostel Fee
Scholarship %
GST %

Print:

Total Fee
Scholarship Amount
Fee After Scholarship
GST Amount
Final Payable Fee


new change in file 
'''

student_name = str(input('Enter Your Full Name  :'))
course = str(input('Enter your course name :'))
tuition_fee = float(input('Enter you tuition fee:'))
exam_fee = float(input('Enter your exam fee:'))
library_fee = float(input('Enter your library fee:'))
hostel_fee = float(input('Enter your hostel fee:'))
scholarship = float(input('Enter your scholarship amount:'))
GST =float(input('enter GST amount:'))

total_fee = (tuition_fee + exam_fee + library_fee + hostel_fee) 
scholarship_amount = total_fee *100/50
fee_after_scholarship = total_fee - scholarship_amount
GST_Amount = fee_after_scholarship * 0.03
finally_payable_amount = fee_after_scholarship + GST_Amount

print('Total Fee :', total_fee)
print('Scholarship Amount :', scholarship)
print('Fee after scholarship :', fee_after_scholarship)
print('GST Amount :', GST_Amount)
print('Finally payable Fee :', finally_payable_amount)
