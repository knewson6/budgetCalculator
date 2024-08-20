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
    additionalIncome = getChar('\nDo you have any other streams of income?', validAnswers2).lower()

    if additionalIncome == 'yes':
        additionalIncomeAmount = getFloat('\nOn average, how much do you make with the other streams of income per month?')
    else:
        additionalIncomeAmount = 0

    monthlyIncome = 0

    if payRate == 'weekly':
        monthlyIncome = (payCheckAmount * 52 / 12) + additionalIncomeAmount
    elif payRate == 'biweekly':
        monthlyIncome = (payCheckAmount * 26 / 12) + additionalIncomeAmount
    elif payRate == 'twice a month':
        monthlyIncome = (payCheckAmount * 2) + additionalIncomeAmount
    elif payRate == 'monthly':
        monthlyIncome = payCheckAmount + additionalIncomeAmount

    return monthlyIncome

def getExpenses():
    expenses = {}

    print('\nWe are now going to ask you for each of your expenses, and their related cost')

    while True:
        expenseName = input('\nEnter the name of the expense (enter "done" if your are finished)\n\t')

        if expenseName == 'done':
            break

        expenseCost = getFloat('How much does this expense cost?')
        expenses[expenseName] = expenseCost

    return expenses