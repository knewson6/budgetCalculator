import tkinter as tk
from tkinter import *
from tkinter import ttk

def frames(root):
    for widget in root.winfo_children():
        widget.destroy()

    headFrame = tk.Frame(root, bg='gray75', width=1200, height=150)
    headFrame.pack(fill='x', side='top')
    headTitle = tk.Label(headFrame, text="Welcome To Your Financial Aid", font=('Times New Roman', 22), bg='gray75', fg='black')
    headTitle.pack(padx=0, pady=20)

    divider = ttk.Separator(root, orient='horizontal')
    divider.pack(fill='x')

    buttonFrame = tk.Frame(root, bg='white', width=1200, height=680)
    buttonFrame.pack(fill='x', side='bottom')

def mainScreen(root):
    root.geometry("1200x680")
    root.title("Personal Financial Assistant")
    root.configure(bg='light gray')

    frames(root)

    budgetPlannerButton = tk.Button(root, text="Budget Planner", font=('Times New Roman', 18), bg='gray85', command=lambda: budgetPlanner(root))
    budgetPlannerButton.place(x=50, y=150, height=200, width=350)

#tracks the progress on the users goals
    savingsTrackerButton = tk.Button(root, text="Savings Tracker", font=('Times New Roman', 18), bg='gray85')
    savingsTrackerButton.place(x=425, y=150, height=200, width=350)

#calculates the amount they earn after tax in their specific area
    taxCalcButton = tk.Button(root, text="Income Tax Calculator", font=('Times New Roman', 18), bg='gray85', command=lambda: taxCalculator(root))
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



def budgetPlanner(root):
    frames(root)

    createFileButton = tk.Button(root, text="Create an Excel File", font=('Times New Roman', 16), bg='gray85', command=lambda: createFile)
    createFileButton.place(x=50, y=200, height=200, width=350)

    editFileButton = tk.Button(root, text="Edit or Manage Files", font=('Times New Roman', 16), bg='gray85', command=lambda: editFile)
    editFileButton.place(x=425, y=200, height=200, width=350)

    noFileButton = tk.Button(root, text="Use Without a File", font=('Times New Roman', 16),bg='gray85', command=lambda: noFile)
    noFileButton.place(x=800, y=200, height=200, width=350)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), bg='gray85', command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    def createFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def editFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def noFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)





def savingsTracker(root):
    for widget in root.winfo_children():
        widget.destroy()





def taxCalculator(root):
    frames(root)

    noticeLabel = tk.Label(root, text="Please Input All Numbers On A Monthly Basis", font=('Times New Roman', 18), bg='white')
    noticeLabel.place(x=350, y=120, height=25, width=500)

    provinces = StringVar(root)
    provinces.set("Pick a Province or Territory")
    provinceMenu = OptionMenu(root, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
    provinceMenu.place(x=125, y=175, height=50, width=225)

    monthlyIncomeLabel = tk.Label(root, text="Monthly Income \n\t\t $", font=('Times New Roman', 18), bg='white')
    monthlyIncomeLabel.place(x=75, y=250)
    monthlyIncome = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    monthlyIncome.place(x=300, y=275)

    rrspContributionLabel = tk.Label(root, text="RRSP Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    rrspContributionLabel.place(x=75, y=325)
    rrspContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    rrspContribution.place(x=300, y=350)

    fhsaContributionLabel = tk.Label(root, text="FHSA Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    fhsaContributionLabel.place(x=75, y=400)
    fhsaContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    fhsaContribution.place(x=300, y=425)

    capitolGainsLabel = tk.Label(root, text="Realised Capitol Gains \n\t\t $", font=('Times New Roman', 18), bg='white')
    capitolGainsLabel.place(x=75, y=475)
    capitolGains = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    capitolGains.place(x=300, y=500)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)





def loanCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()





def debtPayoff(root):
    for widget in root.winfo_children():
        widget.destroy()





def stockGuide(root):
    for widget in root.winfo_children():
        widget.destroy()