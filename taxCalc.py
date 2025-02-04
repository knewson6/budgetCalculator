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
        userMonthlyIncome = monthlyIncome.get().strip()
        userRRSPcontribution = rrspContribution.get().strip()
        userFHSAcontribution = fhsaContribution.get().strip()
        userCapitolGains = capitolGains.get().strip()

        # check user only inputted numbers
        # create a popup error message to let them know to only enter numbers

        return userProvince, userMonthlyIncome, userRRSPcontribution, userFHSAcontribution, userCapitolGains


def provincialTax(userProvince, userMonthlyIncome, userRRSPcontribution, userFHSAcontribution, userCapitolGains):

    income = (userMonthlyIncome * 12) + userCapitolGains - userRRSPcontribution - userFHSAcontribution

    if userProvince == "Ontario":

        taxBracket1 = 52886
        taxRate1 = 0.0505

        taxBracket2 = 105775
        taxRate2 = 0.0915

        taxBracket3 = 150000
        taxRate3 = 0.1116

        taxBracket4 = 220000
        taxRate4 = 0.1216

        taxRate5 = 0.1316

        calculateProvincialTax()

    def calculateProvincialTax(taxBracket1, taxBracket2, taxBracket3, taxBracket4, taxRate1, taxRate2, taxRate3, taxRate4, taxRate5):

    if income <= taxBracket1:
        provincialTaxedIncome = income * taxRate1

    elif taxBracket1 < income <= taxBracket2:
        provincialTaxedIncome = (taxBracket1 * taxRate1) + ((income - taxBracket1) * taxRate2)

    elif taxBracket2 < income <= taxBracket3:
        provincialTaxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((income - taxBracket2) * taxRate3)

    elif taxBracket3 < income <= taxBracket4:
        provincialTaxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((taxBracket3 - taxBracket2) * taxRate3) + ((income - taxBracket3) * taxRate4)

    elif income > taxBracket4:
        provincialTaxedIncome = (taxBracket1 * taxRate1) + ((taxBracket2 - taxBracket1) * taxRate2) + ((taxBracket3 - taxBracket2) * taxRate3) + ((taxBracket4 - taxBracket3) * taxRate4) + ((income - taxBracket4) * taxRate5)

    return provincialTaxedIncome


# def federalTax(provincialTax):
#
#    if provincialTax <= 55867:
#        taxedIncome = provincialTax * 0.85
#    elif 55867 < provincialTax <= 111733:
#        taxedIncome = (55867 * 0.85) + ((provincialTax - 55867) * 0.795)
#    elif 111733 < provincialTax <= 173205:
#        taxedIncome = (55867 * 0.85) + ((provincialTax - 55867) * 0.795) + ((provincialTax - 111733) * 0.74)
#    elif 173205 < provincialTax <= 256752:
#        taxedIncome = (55867 * 0.85) + ((provincialTax - 55867) * 0.795) + ((provincialTax - 111733) * 0.74) + ((provincialTax - 256752) * 0.71)
#    elif provincialTax > 256752:
#        taxedIncome = (55867 * 0.85) + ((provincialTax - 55867) * 0.795) + ((provincialTax - 111733) * 0.74) + ((provincialTax - 256752) * 0.71) + ((provincialTax - 256752) * 0.67)