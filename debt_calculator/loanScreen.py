import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mortgage.mortgageCalc import mortgage
from budgetCalculator.debt_calculator.loan.loanCalculator import loan
from ..sharedFunctions import frames, backButton

def loanScreen(root, mainScreen):
    screen = frames(root)

    mortgageButton = tk.Button(screen, text="Mortgage", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: mortgage())
    mortgageButton.grid(row=0, column=0, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    loanButton = tk.Button(screen, text="Loan", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: loan())
    loanButton.grid(row=0, column=1, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    screen.rowconfigure(0, weight=1)
    screen.columnconfigure(0, weight=1)
    screen.columnconfigure(1, weight=1)

    backButton(mainScreen, lambda: mainScreen(root))