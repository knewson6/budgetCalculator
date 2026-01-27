import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ...sharedFunctions import frames, backButton

def loanCalc():
        from loanScreen import loan_screen
        from financialPlanner import mainScreen
        
        loanFrame = frames(root)

        loanAmountLabel = tk.Label(loanFrame, text="Loan Amount:" + "$".rjust(8), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        loanAmountLabel.place(x=125, y=125)
        loanAmount = tk.Entry(loanFrame, width=15, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        loanAmount.place(x=360, y=128)

        interestRateLabel = tk.Label(loanFrame, text="Interest Rate:" + "%".rjust(4), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        interestRateLabel.place(x=700, y=125)
        interestRate = tk.Entry(loanFrame, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        interestRate.place(x=900, y=128)

        backButton(mainScreen, lambda: loan_screen(root, mainScreen))