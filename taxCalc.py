import tkinter as tk
from tkinter import *
from tkinter import ttk
from sharedFunctions import frames


def taxCalculator(root, mainScreen):
    frames(root)

    noticeLabel = tk.Label(root, text="Please Input All Numbers On A Monthly Basis", font=('Times New Roman', 18), bg='white')
    noticeLabel.place(x=350, y=120, height=25, width=500)

    provinces = StringVar(root)
    provinces.set("Pick a Province or Territory")
    provinceMenu = OptionMenu(root, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
    provinceMenu.place(x=125, y=175, height=50, width=225)

    monthlyIncomeLabel = tk.Label(root, text="Monthly Income \n\t\t $", font=('Times New Roman', 18), bg='white')
    monthlyIncomeLabel.place(x=75, y=250)
    monthlyIncome = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    monthlyIncome.place(x=300, y=275)

    rrspContributionLabel = tk.Label(root, text="RRSP Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    rrspContributionLabel.place(x=75, y=325)
    rrspContribution = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    rrspContribution.place(x=300, y=350)

    fhsaContributionLabel = tk.Label(root, text="FHSA Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    fhsaContributionLabel.place(x=75, y=400)
    fhsaContribution = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    fhsaContribution.place(x=300, y=425)

    capitolGainsLabel = tk.Label(root, text="Realised Capitol Gains \n\t\t $", font=('Times New Roman', 18), bg='white')
    capitolGainsLabel.place(x=75, y=475)
    capitolGains = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    capitolGains.place(x=300, y=500)

    calculateButton = tk.Button(root, text="Calculate!", font=('Times New Roman', 12), command=lambda: getUserInput())
    calculateButton.place(x=800, y=600, height=50, width=100)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    def getUserInput():

        userProvince = provinces.get()

        if monthlyIncome.get().replace(",","").replace(".","",1).isdigit():
            userMonthlyIncome = float(monthlyIncome.get().strip() or 0)
        #else create an error popup

        if rrspContribution.get().replace(",", "").replace(".", "", 1).isdigit():
            userRRSPcontribution = float(rrspContribution.get().strip() or 0)
        #else create an error popup

        if fhsaContribution.get().replace(",", "").replace(".", "", 1).isdigit():
            userFHSAcontribution = float(fhsaContribution.get().strip() or 0)
        #else create an error popup

        if capitolGains.get().replace(",", "").replace(".", "", 1).isdigit():
            userCapitolGains = float(capitolGains.get().strip() or 0)
        #else create an error popup


        income = (userMonthlyIncome * 12) + userCapitolGains - userRRSPcontribution - userFHSAcontribution

        if userProvince == "Ontario":
            ontarioTax = calculateTax(income, 52886, 105775, 150000, 220000, 0.0505, 0.0915, 0.1116, 0.1216, 0.1316)
            federalTax = calculateTax(income, 57375, 114750, 177882, 253414, 0.15, 0.205, 0.26, 0.29, 0.33)



def calculateTax(income, taxBracket1, taxBracket2, taxBracket3, taxBracket4, taxRate1, taxRate2, taxRate3, taxRate4, taxRate5):

    #if you make more than 67,800, your max CPP limit is 3500, below that it is 4.91% of your income (its 5.95% for employer and employee to pay, but ive made it 4.91 for the user)
    #if you make more than 65,700, your max EI limit is 1077.48, below that is 1.67% of your income

    if income <= taxBracket1:
        taxedIncome = income * taxRate1

    elif taxBracket1 < income <= taxBracket2:
        taxedIncome = (taxBracket1 * taxRate1) + ((income - taxBracket1) * taxRate2)

    elif taxBracket2 < income <= taxBracket3:
        taxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((income - taxBracket2) * taxRate3)

    elif taxBracket3 < income <= taxBracket4:
        taxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((taxBracket3 - taxBracket2) * taxRate3) + ((income - taxBracket3) * taxRate4)

    elif income > taxBracket4:
        taxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((taxBracket3 - taxBracket2) * taxRate3) + ((taxBracket4 - taxBracket3) * taxRate4) + ((income - taxBracket4) * taxRate5)

        return taxedIncome
