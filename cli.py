from pay_period import pay_period
from tax_calculation import *
from user_details import user_details


print("Welcome to payslip generator!")

user_details()
gross_inc, annual_sal = gross_income()
my_super = super_k(gross_inc)
inc_tax = income_tax(annual_sal)
net_inc = net_income(gross_inc, inc_tax)
start_date = pay_period()
print('\n')
print("***********************")
print(f'PAY PERIOD:\t 1st of {start_date} to 30st of {start_date}')
print(f"Gross Income:\t{gross_inc}")
print(f"Income Tax: \t{inc_tax}")
print(f"Net Income: \t{net_inc}")
print(f"Super:\t\t{my_super}")
print('\n')
print('\n')
print("Thank you for using MYOB")
print('\n')
print("***********************")