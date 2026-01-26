import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from debt_calculator.mortgage.mortgageCalculator import mortgageCalc
from loan.loanCalculator import loanCalc
from ..sharedFunctions import frames, backButton

def loan_screen(root, mainScreen):
    screen = frames(root)

    mortgageButton = tk.Button(screen, text="Mortgage", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: mortgageCalc())
    mortgageButton.grid(row=0, column=0, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    loanButton = tk.Button(screen, text="Loan", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: loanCalc())
    loanButton.grid(row=0, column=1, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    screen.rowconfigure(0, weight=1)
    screen.columnconfigure(0, weight=1)
    screen.columnconfigure(1, weight=1)

    backButton(mainScreen, lambda: mainScreen(root))