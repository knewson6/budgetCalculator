from multiprocessing.managers import Value

import numpy as np
import math

def QNA():
    validPayRate = ['weekly', 'biweekly', 'bi-weekly', 'bi weekly', 'twice a month', 'monthly']

    while True:
        payRate = input('How often do you get paid?\n\t').lower()

        if payRate not in validPayRate:
            print('Error Input; please enter weekly or biweekly or bi weekly or bi-weekly or twice a month or monthly')
        else:
            break

    while True:
        try:
            payAmount = float(input('On average how much is each pay cheque?\n\t$'))

            if payAmount <= 0:
                print('Error Input; please enter a non negative number')
            else:
                break
        except ValueError:
            print('Error Input; please enter a non negative number with no special characters or letters')