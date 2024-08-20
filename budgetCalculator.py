import numpy as np
import math
from budgetCalculatorFunctions import getChar, getFloat, getExpenses, getIncome, getSavings, getTaxDeductibleSavings, federalTax, provincialTax

monthlyIncome = getIncome()
expenses = getExpenses()
savings = getSavings()
taxDeductibleSavings = getTaxDeductibleSavings()
fedTaxedIncome = federalTax(monthlyIncome, taxDeductibleSavings)
provincialTax = provincialTax(fedTaxedIncome)