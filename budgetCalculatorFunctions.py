import numpy as np
import math

def getChar(prompt, validInput):

    while True:
        userInput = input(prompt + '\n\t').lower()

        if userInput not in validInput:
            print('Error Input; please enter one of', validInput)
        else:
            return userInput

def getFloat(prompt):

    while True:
        try:
            userInput = float(input(prompt + '\n\t$'))

            if userInput <= 0:
                print('Error Input; please enter a non negative number')
            else:
                return userInput
        except ValueError:
            print('Error Input; please enter a non negative number with no special characters or letters')

def getIncome():
    validAnswers = ['weekly', 'biweekly', 'twice a month', 'monthly']
    payRate = getChar('\nHow often do you get paid?', validAnswers).lower()

    payCheckAmount = getFloat('\nOn average, how much is each paycheck?')

    validAnswers2 = ['yes', 'no']
    otherIncome = getChar('\nDo you have any other streams of income?', validAnswers2).lower()

    if otherIncome == 'yes':
        otherIncomeAmount = getFloat('\nOn average, how much do you make with the other streams of income per month?')
    else:
        otherIncomeAmount = 0

    monthlyIncome = 0

    if payRate == 'weekly':
        monthlyIncome = (payCheckAmount * 52 / 12) + otherIncomeAmount
    elif payRate == 'biweekly':
        monthlyIncome = (payCheckAmount * 26 / 12) + otherIncomeAmount
    elif payRate == 'twice a month':
        monthlyIncome = (payCheckAmount * 2) + otherIncomeAmount
    elif payRate == 'monthly':
        monthlyIncome = payCheckAmount + otherIncomeAmount

    return monthlyIncome

def getExpenses():
    expenses = {}

    while True:
        expenseName = input('\nEnter the name of an expense (enter "done" if your are finished)\n\t')

        if expenseName == 'done':
            break

        expenseCost = getFloat('\nHow much does this expense cost?')

        expenses[expenseName] = expenseCost

    return expenses

def getTaxDeductibleSavings():
    taxDeductibleSavings = {}

    while True:
        taxDeductibleSavingsName = input('\nEnter the name of any the tax deductible savings account(s) (enter "done" if you are finished)\n\t')

        if taxDeductibleSavingsName == 'done':
            break

        taxDeductibleSavingsCost = getFloat('\nHow much do you put away into this account?')

        taxDeductibleSavings[taxDeductibleSavingsName] = taxDeductibleSavingsCost

    return taxDeductibleSavings

def getSavings():
    savings = {}

    while True:
        savingsName = input('\nEnter the name of any savings account(s) (enter "done" if you are finished)\n\t')

        if savingsName == 'done':
            break

        savingsCost = getFloat('\nHow much do you put away into this account?')

        savings[savingsName] = savingsCost

    return savings

def federalTax(monthlyIncome, taxDeductibleSavings):

    income = (monthlyIncome * 12) - taxDeductibleSavings
    fedTaxedIncome = 0

    if income <= 55867:
        fedTaxedIncome = income * 0.85
    elif 55867 < income <= 111733:
        fedTaxedIncome = (55867 * 0.85) + ((income - 55867) * 0.795)
    elif 111733 < income <= 173205:
        fedTaxedIncome = (55867 * 0.85) + ((income - 55867) * 0.795) + ((income - 111733) * 0.74)
    elif 173205 < income <= 256752:
        fedTaxedIncome = (55867 * 0.85) + ((income - 55867) * 0.795) + ((income - 111733) * 0.74) + ((income - 256752) * 0.71)
    elif income > 256752:
        fedTaxedIncome = (55867 * 0.85) + ((income - 55867) * 0.795) + ((income - 111733) * 0.74) + ((income - 256752) * 0.71) + ((income - 256752) * 0.67)

    return fedTaxedIncome

def provincialTax(fedTaxedIncome):

    taxedIncome = 0

    if fedTaxedIncome <= 51446:
        taxedIncome = fedTaxedIncome * 0.0505
    elif 51446 < fedTaxedIncome <= 102894:
        taxedIncome = (fedTaxedIncome * 0.9495) + ((fedTaxedIncome - 51446) * 0.9085)
    elif 102894 < fedTaxedIncome <= 150000:
        taxedIncome = (fedTaxedIncome * 0.9495) + ((fedTaxedIncome - 51446) * 0.9085) + ((fedTaxedIncome - 102894) * 0.8884)
    elif 150000 < fedTaxedIncome <= 220000:
        taxedIncome = (fedTaxedIncome * 0.9495) + ((fedTaxedIncome - 51446) * 0.9085) + ((fedTaxedIncome - 102894) * 0.8884) + ((fedTaxedIncome - 150000) * 0.8784)
    elif fedTaxedIncome > 220000:
        taxedIncome = (fedTaxedIncome * 0.9495) + ((fedTaxedIncome - 51446) * 0.9085) + ((fedTaxedIncome - 102894) * 0.8884) + ((fedTaxedIncome - 150000) * 0.8784) + ((fedTaxedIncome - 220000) * 0.8684)

    return taxedIncome