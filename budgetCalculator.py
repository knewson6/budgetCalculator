import numpy as np
import math
from budgetCalculatorFunctions import getChar
from budgetCalculatorFunctions import getFloat

validAnswers = ['weekly', 'biweekly', 'bi weekly', 'bi weekly', 'twice a month', 'monthly']
payRate = getChar('\nHow often do you get paid?', validAnswers)

payCheckAmount = getFloat('\nOn average, how much is each paycheck?')
