import numpy as np
import math
from budgetCalculatorFunctions import getChar, getFloat, getExpenses, getIncome, getSavings, getTaxDeductibleSavings, federalTax, provincialTax


print('\nWelcome to our Canadian Budget Calculator')
print('1) Start a new file')
print('2) Update an old file')
print('3) Delete an old file')
print('4) Use the calculator without a file')
print('5) Exit')

userInput = input('\n\tHow can we assist? : ')

if userInput == '4':
    income = getIncome()
    expenses = getExpenses()
    taxDeductibles = getTaxDeductibleSavings()
    savings = getSavings()
    federalTax = federalTax(income, taxDeductibles)
    taxedIncome = provincialTax(federalTax)