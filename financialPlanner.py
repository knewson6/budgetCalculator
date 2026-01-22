# Kyle Newson
# Start Date = Feb 3, 2025

import tkinter as tk
from tkinter import *
from tkinter import ttk
from Budget.budgetPlanner import budgetPlanner
from Tax_Calculator.taxCalc import taxCalculator
from Loan_Calculator.loanCalc import loanCalculator
from sharedFunctions import frames

def mainScreen(root):

    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    buttonFrame = frames(root)

    buttons = [
        ("Budget Planner", lambda: budgetPlanner(root, mainScreen)),
        ("Savings Tracker", None),
        ("Income Tax Calculator", lambda: taxCalculator(root, mainScreen)),
        ("Loan/Mortgage Calculator", lambda: loanCalculator(root, mainScreen)),
        ("Debt Payoff Calculator", None),
        ("Stock Guide", None)
    ]

    for index, (text, cmd) in enumerate(buttons):
        row, col = divmod(index, 3)
        button = tk.Button(buttonFrame, text=text, font=('Times New Roman', 18), bg='gray85', command=cmd if cmd else None)
        button.grid(row=row, column=col, padx=10, pady=25, sticky="nsew")

    for i in range(2):
        buttonFrame.rowconfigure(i, weight=1, uniform="row")
    for j in range(3):
        buttonFrame.columnconfigure(j, weight=1, uniform="col")

def startUp():
    root = tk.Tk()
    root.geometry("1200x680")
    mainScreen(root)
    root.mainloop()

startUp()