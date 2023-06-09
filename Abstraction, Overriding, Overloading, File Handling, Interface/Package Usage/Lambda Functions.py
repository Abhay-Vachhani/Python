# Find gross salary using package

# Import Calculator module and its functions form the SalaryCalculator package

# from SalaryCalculator.Calculator import calc_da, calc_pf, calc_ta
from SalaryCalculator.Calculator import *
# from SalaryCalculator import Calculator
# Calculator.calc_da(...)

basicSalary = int(input('Enter basic salary: '))

grossSalary = basicSalary + calc_da(basicSalary) + calc_ta(basicSalary) - calc_pf(basicSalary)

print('DA: ', calc_da(basicSalary))
print('TA: ', calc_ta(basicSalary))
print('PF: ', calc_pf(basicSalary))
print('Gross Salary:', grossSalary)