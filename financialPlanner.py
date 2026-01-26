# Kyle Newson
# Start Date = Feb 3, 2025

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import *
from tkinter import ttk
from sharedFunctions import frames
from tax_calculator.taxCalculator import taxCalc
from debt_calculator.loan.loanCalculator import loan_screen

def mainScreen(root):

    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    buttonFrame = frames(root)

    buttons = [
        ("Budget Planner", None),
        ("Savings Tracker", None),
        ("Income Tax Calculator", lambda: taxCalc(root, mainScreen)),
        ("Loan/Mortgage Calculator", lambda: loan_screen(root, mainScreen)),
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