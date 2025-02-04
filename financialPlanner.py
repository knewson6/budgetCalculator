# Kyle Newson
# Feb 3, 2025

import tkinter as tk
from tkinter import *
from tkinter import ttk
from budgetPlanner import budgetPlanner
from taxCalc import taxCalculator
from sharedFunctions import frames

def mainScreen(root):

    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    frames(root)

#budget planner for the user, and ability to create or edit/manage files
    budgetPlannerButton = tk.Button(root, text="Budget Planner", font=('Times New Roman', 18), bg='gray85', command=lambda: budgetPlanner(root, mainScreen))
    budgetPlannerButton.place(x=50, y=150, height=200, width=350)

#tracks the progress on the users goals
    savingsTrackerButton = tk.Button(root, text="Savings Tracker", font=('Times New Roman', 18), bg='gray85')
    savingsTrackerButton.place(x=425, y=150, height=200, width=350)

#calculates the amount they earn after tax in their specific area
    taxCalcButton = tk.Button(root, text="Income Tax Calculator", font=('Times New Roman', 18), bg='gray85', command=lambda: taxCalculator(root, mainScreen))
    taxCalcButton.place(x=800, y=150, height=200, width=350)

#goes into loan or mortgage and breaks down the interest and premium paid over the timeframe
    loanCalc = tk.Button(root, text="Loan/Mortgage Calculator", font=('Times New Roman', 18), bg='gray85')
    loanCalc.place(x=50, y=375, height=200, width=350)

#creates a plan to pay off a debt (or a certain amount) by a specific date
    debtPayoffButton = tk.Button(root, text="Debt Payoff Plan", font=("Times New Roman", 18), bg='gray85')
    debtPayoffButton.place(x=425, y=375, height=200, width=350)

#gives insight on which stokes to buy and when
    stockGuideButton = tk.Button(root, text="Stock Guide", font=("Times New Roman", 18), bg='gray85')
    stockGuideButton.place(x=800, y=375, height=200, width=350)

def startUp():
    root = tk.Tk()
    root.geometry("1200x680")
    mainScreen(root)
    root.mainloop()

startUp()