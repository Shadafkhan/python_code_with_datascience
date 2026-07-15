'''Employee Payroll Generator

Take:

Employee Name
Employee ID
Basic Salary
HRA %
DA %
Travel Allowance
Medical Allowance
PF %
Professional Tax

Calculate:

Gross Salary
PF Deduction
Net Salary

Print a professional salary slip.'''

# Employee Payroll Generator

employee_name = input("Enter your name: ")
employee_id = input("Enter your ID: ")

basic_salary = float(input("Enter your monthly salary: "))
hra = float(input("Enter HRA (%): "))
da = float(input("Enter DA (%): "))
travel_allowance = float(input("Enter Travel Allowance: "))
medical_allowance = float(input("Enter Medical Allowance: "))
pf = float(input("Enter PF (%): "))
professional_tax = float(input("Enter Professional Tax: "))

# Calculate Allowances
hra_allowance = basic_salary * (hra / 100)
da_allowance = basic_salary * (da / 100)

# Gross Salary
gross_salary = (
    basic_salary
    + hra_allowance
    + da_allowance
    + travel_allowance
    + medical_allowance
)

# Deductions
pf_deduction = basic_salary * (pf / 100)
total_deduction = pf_deduction + professional_tax

# Net Salary
net_salary = gross_salary - total_deduction

# Salary Slip
print("\n===================================")
print("       EMPLOYEE SALARY SLIP")
print("===================================")
print("Employee Name      :", employee_name)
print("Employee ID        :", employee_id)
print("-----------------------------------")
print("Basic Salary       :", basic_salary)
print("HRA Amount         :", hra_allowance)
print("DA Amount          :", da_allowance)
print("Travel Allowance   :", travel_allowance)
print("Medical Allowance  :", medical_allowance)
print("-----------------------------------")
print("Gross Salary       :", gross_salary)
print("PF Deduction       :", pf_deduction)
print("Professional Tax   :", professional_tax)
print("Total Deduction    :", total_deduction)
print("-----------------------------------")
print("Net Salary         :", net_salary)
print("===================================")