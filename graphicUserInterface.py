import tkinter as tk
from tkinter import ttk

def graphicUI():
    root = tk.Tk()

    root.geometry("1200x680")
    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    def mainScreen():
        for widget in root.winfo_children():
            widget.destroy()

        headFrame = tk.Frame(root, bg='gray75', width=1200, height=150)
        headFrame.pack(fill='x', side='top')
        headTitle = tk.Label(headFrame, text="Welcome To Your Financial Aid", font=('Times New Roman', 22), bg='gray75',
                             fg='black')
        headTitle.pack(padx=0, pady=20)

        divider = ttk.Separator(root, orient='horizontal')
        divider.pack(fill='x')

        buttonFrame = tk.Frame(root, bg='floral white', width=1200, height=680)
        buttonFrame.pack(fill='x', side='bottom')

#goes into another button to create or edit/manage files or use without
        budgetPlannerButton = tk.Button(root, text="Budget Planner", font=('Times New Roman', 18), command=budgetPlanner)
        budgetPlannerButton.place(x=50, y=150, height=200, width=350)

#tracks the progress on the users goals
        savingsTrackerButton = tk.Button(root, text="Savings Tracker", font=('Times New Roman', 18))
        savingsTrackerButton.place(x=425, y=150, height=200, width=350)

#calculates the amount they earn after tax in their specific area
        taxCalcButton = tk.Button(root, text="Income Tax Calculator", font=('Times New Roman', 18))
        taxCalcButton.place(x=800, y=150, height=200, width=350)

#goes into loan or mortgage and breaks down the interest and premium paid over the timeframe
        loanCalc = tk.Button(root, text="Loan/Mortgage Calculator", font=('Times New Roman', 18))
        loanCalc.place(x=50, y=375, height=200, width=350)

#creates a plan to pay off a debt (or a certain amount) by a specific date
        debtPayoffButton = tk.Button(root, text="Debt Payoff Plan", font=("Times New Roman", 18))
        debtPayoffButton.place(x=425, y=375, height=200, width=350)

#gives insight on which stokes to buy and when
        stockGuideButton = tk.Button(root, text="Stock Guide", font=("Times New Roman", 18))
        stockGuideButton.place(x=800, y=375, height=200, width=350)

    def budgetPlanner():
        for widget in root.winfo_children():
            widget.destroy()

        headFrame = tk.Frame(root, bg='gray75', width=1200, height=150)
        headFrame.pack(fill='x', side='top')
        headTitle = tk.Label(headFrame, text="Budget Planner", font=('Times New Roman', 22), bg='gray75',fg='black')
        headTitle.pack(padx=0, pady=20)

        divider = ttk.Separator(root, orient='horizontal')
        divider.pack(fill='x')

        buttonFrame = tk.Frame(root, bg='floral white', width=1200, height=680)
        buttonFrame.pack(fill='x', side='bottom')

        createFileButton = tk.Button(root, text="Create an Excel File", font=('Times New Roman', 16))
        createFileButton.place(x=50, y=200, height=200, width=350)

        editFileButton = tk.Button(root, text="Edit or Manage Files", font=('Times New Roman', 16))
        editFileButton.place(x=425, y=200, height=200, width=350)

        noFileButton = tk.Button(root, text="Use Without a File", font=('Times New Roman', 16))
        noFileButton.place(x=800, y=200, height=200, width=350)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=mainScreen)
        backButton.place(x=1050, y=600, height=50, width=100)

    def savingsTracker():
        for widget in root.winfo_children():
            widget.destroy()

    def taxCalculator():
        for widget in root.winfo_children():
            widget.destroy()

    def loanCalculator():
        for widget in root.winfo_children():
            widget.destroy()

    def debtPayoff():
        for widget in root.winfo_children():
            widget.destroy()

    def stockGuide():
        for widget in root.winfo_children():
            widget.destroy()

    mainScreen()
    root.mainloop()

graphicUI()