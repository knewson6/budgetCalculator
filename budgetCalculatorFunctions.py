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

def getExpenses()

