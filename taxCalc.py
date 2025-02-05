import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sharedFunctions import frames


def taxCalculator(root, mainScreen):
    frames(root)

    noticeLabel = tk.Label(root, text="Please Input All Numbers On A Monthly Basis", font=('Times New Roman', 22), bg='white')
    noticeLabel.place(x=300, y=120, height=30, width=600)

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

    capitalGainsLabel = tk.Label(root, text="Realised capital Gains \n\t\t $", font=('Times New Roman', 18), bg='white')
    capitalGainsLabel.place(x=75, y=475)
    capitalGains = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    capitalGains.place(x=300, y=500)

    calculateButton = tk.Button(root, text="Calculate!", font=('Times New Roman', 20), command=lambda: getUserInput())
    calculateButton.place(x=75, y=575, height=50, width=355)

    netIncomeLabel = tk.Label(root, text="Net Income : $ 0.00", font=('Times New Roman', 18), bg='white')
    netIncomeLabel.place(x=800, y=350)

    provincialTaxesLabel = tk.Label(root, text="Provincial Taxes: $ 0.00 ", font=('Times New Roman', 18), bg='white')
    provicinalTaxesLabel.place(x=500, y=450)

    federalTaxesLabel = tk.Label(root, text="Provincial Taxes: $ 0.00 ", font=('Times New Roman', 18), bg='white')
    federalTaxesLabel.place(x=500, y=550)

    #take home income
    #fed taxes paid
    #prov taxes paid

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    def getUserInput():

        userProvince = provinces.get()
        if userProvince == "Pick a Province or Territory":
            messagebox.showerror("Input Error", "Please select a province.")
            return

        try:
            userMonthlyIncome = float(monthlyIncome.get().replace(",", "").replace(".", "", 1).strip() or 0)
            userRRSPcontribution = float(rrspContribution.get().replace(",", "").replace(".", "", 1).strip() or 0)
            userFHSAcontribution = float(fhsaContribution.get().replace(",", "").replace(".", "", 1).strip() or 0)
            userCapitalGains = float(capitalGains.get().replace(",", "").replace(".", "", 1).strip() or 0)
        except ValueError:
            messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
            return

        income = (userMonthlyIncome * 12) + userCapitalGains - userRRSPcontribution - userFHSAcontribution

        if userProvince == "Ontario":

            provincialTax = calculateTax(income, 52886, 105775, 150000, 220000, 0.0505, 0.0915, 0.1116, 0.1216, 0.1316)
            federalTax = calculateTax(income, 57375, 114750, 177882, 253414, 0.15, 0.205, 0.26, 0.29, 0.33)

        else:
            exit()


        netIncomeLabel.config(text=f"Net Income: $ {income:.2f}")
        provicialTaxesLabel.config(text=f"Provincial Taxes : $ {provincialTax:.2f}")
        federalTaxesLabel.config(text=f"Federal Taxes : $ {federalTax:.2f}")

        return


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
