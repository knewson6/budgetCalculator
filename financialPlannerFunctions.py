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

# def ontarioTax():
#
#     taxedIncome = 0
#
#     if taxedIncome <= 51446:
#         provincialTaxedIncome = taxedIncome * 0.0505
#     elif 51446 < taxedIncome <= 102894:
#         provincialTaxedIncome = (taxedIncome * 0.9495) + ((taxedIncome - 51446) * 0.9085)
#     elif 102894 < taxedIncome <= 150000:
#         provincialTaxedIncome = (taxedIncome * 0.9495) + ((taxedIncome - 51446) * 0.9085) + ((taxedIncome - 102894) * 0.8884)
#     elif 150000 < taxedIncome <= 220000:
#         provincialTaxedIncome = (taxedIncome * 0.9495) + ((taxedIncome - 51446) * 0.9085) + ((taxedIncome - 102894) * 0.8884) + ((taxedIncome - 150000) * 0.8784)
#     elif taxedIncome > 220000:
#         provincialTaxedIncome = (taxedIncome * 0.9495) + ((taxedIncome - 51446) * 0.9085) + ((taxedIncome - 102894) * 0.8884) + ((taxedIncome - 150000) * 0.8784) + ((taxedIncome - 220000) * 0.8684)
#
#     return provincialTaxedIncome