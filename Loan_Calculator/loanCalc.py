import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mortgage_calculator import mortgage
from sharedFunctions import frames, backButton

def loanCalculator(root, mainScreen):
    loanCalc = frames(root)

    mortgageButton = tk.Button(loanCalc, text="Mortgage", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: mortgage())
    mortgageButton.grid(row=0, column=0, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    loanButton = tk.Button(loanCalc, text="Loan", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: loan())
    loanButton.grid(row=0, column=1, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    loanCalc.rowconfigure(0, weight=1)
    loanCalc.columnconfigure(0, weight=1)
    loanCalc.columnconfigure(1, weight=1)

    backButton(mainScreen, lambda: mainScreen(root))