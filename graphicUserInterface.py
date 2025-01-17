import tkinter as tk
from tkinter import *
from tkinter import ttk
from guiFunctions import frames


def graphicUI():
    root = tk.Tk()

    root.geometry("1200x680")
    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    def mainScreen():

        frames(root)

        budgetPlannerButton = tk.Button(root, text="Budget Planner", font=('Times New Roman', 18), bg='gray85' ,command=budgetPlanner)
        budgetPlannerButton.place(x=50, y=150, height=200, width=350)

#tracks the progress on the users goals
        savingsTrackerButton = tk.Button(root, text="Savings Tracker", font=('Times New Roman', 18), bg='gray85')
        savingsTrackerButton.place(x=425, y=150, height=200, width=350)

#calculates the amount they earn after tax in their specific area
        taxCalcButton = tk.Button(root, text="Income Tax Calculator", font=('Times New Roman', 18), bg='gray85', command=taxCalculator)
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





    def budgetPlanner():

        frames(root)

        createFileButton = tk.Button(root, text="Create an Excel File", font=('Times New Roman', 16), bg='gray85', command=createFile)
        createFileButton.place(x=50, y=200, height=200, width=350)

        editFileButton = tk.Button(root, text="Edit or Manage Files", font=('Times New Roman', 16), bg='gray85', command=editFile)
        editFileButton.place(x=425, y=200, height=200, width=350)

        noFileButton = tk.Button(root, text="Use Without a File", font=('Times New Roman', 16),bg='gray85', command=noFile)
        noFileButton.place(x=800, y=200, height=200, width=350)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), bg='gray85', command=mainScreen)
        backButton.place(x=1050, y=600, height=50, width=100)

    def createFile():

        frames(root)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=budgetPlanner)
        backButton.place(x=1050, y=600, height=50, width=100)

    def editFile():

        frames(root)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=budgetPlanner)
        backButton.place(x=1050, y=600, height=50, width=100)

    def noFile():

        frames(root)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=budgetPlanner)
        backButton.place(x=1050, y=600, height=50, width=100)





    def savingsTracker():
        for widget in root.winfo_children():
            widget.destroy()





    def taxCalculator():

        frames(root)

        backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=mainScreen)
        backButton.place(x=1050, y=600, height=50, width=100)

        provinces = StringVar(root)
        provinces.set("Pick a Province or Territory")
        provinceMenu = OptionMenu(root, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
        provinceMenu.place(x=480, y=125, height=50, width=225)

        monthlyIncomeLabel = tk.Label(root, text="Monthly Income \n\t\t $", font=('Times New Roman', 18), bg='white')
        monthlyIncomeLabel.place(x=75, y=200)
        monthlyIncome = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        monthlyIncome.place(x=290, y=225)

        rrspContributionLabel = tk.Label(root, text="RRSP Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
        rrspContributionLabel.place(x=75, y=275)
        rrspContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        rrspContribution.place(x=290, y=300)

        fhsaContributionLabel = tk.Label(root, text="FHSA Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
        fhsaContributionLabel.place(x=75, y=350)
        fhsaContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        fhsaContribution.place(x=290, y=375)

        capitolGainsLabel = tk.Label(root, text="Capitol Gains \n\t\t $", font=('Times New Roman', 18), bg='white')
        capitolGainsLabel.place(x=75, y=425)
        capitolGains = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        capitolGains.place(x=290, y=450)



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