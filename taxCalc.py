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

    monthlyIncomeLabel = tk.Label(root, text="Employment Income \n" + "$".rjust(36), font=('Times New Roman', 18), bg='white', width=50, anchor="w", justify="left")
    monthlyIncomeLabel.place(x=75, y=250)
    monthlyIncome = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    monthlyIncome.place(x=315, y=280)

    rrspContributionLabel = tk.Label(root, text="RRSP Contribution \n" + "$".rjust(36), font=('Times New Roman', 18), bg='white', width=50, anchor="w", justify="left")
    rrspContributionLabel.place(x=75, y=325)
    rrspContribution = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    rrspContribution.place(x=315, y=355)

    fhsaContributionLabel = tk.Label(root, text="FHSA Contribution \n" + "$".rjust(36), font=('Times New Roman', 18), bg='white', width=50, anchor="w", justify="left")
    fhsaContributionLabel.place(x=75, y=400)
    fhsaContribution = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    fhsaContribution.place(x=315, y=430)

    capitalGainsLabel = tk.Label(root, text="Capital Gains \n" + "$".rjust(36), font=('Times New Roman', 18), bg='white', width=50, anchor="w", justify="left")
    capitalGainsLabel.place(x=75, y=475)
    capitalGains = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    capitalGains.place(x=315, y=505)

    calculateButton = tk.Button(root, text="Calculate!", font=('Times New Roman', 20), command=lambda: getUserInput())
    calculateButton.place(x=75, y=575, height=50, width=370)

    takeHomeLabel = tk.Label(root, text="Take Home Pay: $ 0.00 ", font=('Times New Roman', 22), bg='white')
    takeHomeLabel.place(x=700, y=225)

    grossIncomeLabel = tk.Label(root, text="Gross Income: $ 0.00", font=('Times New Roman', 15), bg='white')
    grossIncomeLabel.place(x=797, y=275)

    provincialTaxesLabel = tk.Label(root, text="Provincial Taxes: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    provincialTaxesLabel.place(x=771, y=315)

    federalTaxesLabel = tk.Label(root, text="Federal Taxes: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    federalTaxesLabel.place(x=792, y=355)

    cppContributionLabel = tk.Label(root, text="CPP Contribution: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    cppContributionLabel.place(x=766, y=395)

    eiContributionLabel = tk.Label(root, text="EI Contribution: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    eiContributionLabel.place(x=784, y= 435)

    fhsaDeductionLabel = tk.Label(root, text="FHSA Deduction: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    fhsaDeductionLabel.place(x=769, y=475)

    rrspDeductionLabel = tk.Label(root, text="RRSP Deduction: $ 0.00 ", font=('Times New Roman', 15), bg='white')
    rrspDeductionLabel.place(x=772, y=515)

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

        rrspDeduction = min((userRRSPcontribution * 12), (userMonthlyIncome * 12 * 0.18), 31560)
        fhsaDeduction = min((userFHSAcontribution * 12),8000)
        income = (userMonthlyIncome * 12) + userCapitalGains - rrspDeduction - fhsaDeduction

        if userProvince == "Alberta":

            provincialTaxBracket = [60000, 151234, 181481, 241974, 362961]
            provincialTaxRate = [0.08, 0.10, 0.12, 0.13, 0.14, 0.15]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "British Columbia":

            provincialTaxBracket = [49279, 98560, 113158, 137407, 186306, 259829]
            provincialTaxRate = [0.0506, 0.077, 0.105, 0.1229, 0.147, 0.168, 0.205]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Manitoba":

            provincialTaxBracket = [47564, 101200]
            provincialTaxRate = [0.108, 0.1275, 0.174]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "New Brunswick":

            provincialTaxBracket = [51306, 102614, 190060]
            provincialTaxRate = [0.094, 0.14, 0.16, 0.195]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Newfoundland and Labrador":

            provincialTaxBracket = [44192, 88382, 157792, 220910, 282214, 564429, 1128858]
            provincialTaxRate = [0.087, 0.145, 0.158, 0.178, 0.198, 0.208, 0.213, 0.218]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Nova Scotia":

            provincialTaxBracket = [30507, 61015, 95883, 154650]
            provincialTaxRate = [0.0879, 0.1495, 0.1667, 0.175, 0.21]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Northwest Territories":

            provincialTaxBracket = [51964, 103930, 168967]
            provincialTaxRate = [0.059, 0.086, 0.122, 0.1405]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Nunavut":

            provincialTaxBracket = [54707, 109413, 177881]
            provincialTaxRate = [0.04, 0.07, 0.09, 0.115]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Ontario":

            provincialTaxBracket = [52886, 105775 ,150000, 220000]
            provincialTaxRate = [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Prince Edward Island":

            provincialTaxBracket = [33328, 64656, 105000, 140000]
            provincialTaxRate = [0.095, 0.1347, 0.166, 0.1762, 0.19]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Quebec":

            provincialTaxBracket = [53225, 106495, 129590]
            provincialTaxRate = [0.14, 0.19, 0.24, 0.2575]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Saskatchewan":

            provincialTaxBracket = [53462, 152750]
            provincialTaxRate = [0.105, 0.125, 0.145]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        elif userProvince == "Yukon":

            provincialTaxBracket = [57375, 114750, 177882, 500000]
            provincialTaxRate = [0.064, 0.09, 0.109, 0.128, 0.15]
            provincialTax = calculateTax(income, provincialTaxBracket, provincialTaxRate)

            federalTaxBracket = [57375, 114750, 177882, 253414]
            federalTaxRate = [0.145, 0.205, 0.26, 0.29, 0.33]
            federalTax = calculateTax(income, federalTaxBracket, federalTaxRate)

        else:
            exit()

        if income <=67800:
            cppContribution = income * 0.0491
        else:
            cppContribution = 3500

        if income <= 65700:
            eiContribution = income * 0.0167
        else:
            eiContribution = 1077.48

        takeHome = income - federalTax - provincialTax - cppContribution - eiContribution

        grossIncomeLabel.config(text=f"Gross Income: $ {income:.2f}")
        provincialTaxesLabel.config(text=f"Provincial Taxes : $ {provincialTax:.2f}")
        federalTaxesLabel.config(text=f"Federal Taxes : $ {federalTax:.2f}")
        cppContributionLabel.config(text=f"CPP Contribution : $ {cppContribution:.2f}")
        eiContributionLabel.config(text=f"EI Contribution : $ {eiContribution:.2f}")
        rrspDeductionLabel.config(text=f"RRSP Deduction : $ {rrspDeduction:.2f}")
        fhsaDeductionLabel.config(text=f"FHSA Deduction : $ {fhsaDeduction:.2f}")
        takeHomeLabel.config(text=f"Take Home Pay: $ {takeHome:.2f}")

        return


def calculateTax(income, taxBracket, taxRate):

    tax = 0
    previousBracket = 0

    for i in range(len(taxBracket)):
        if income > taxBracket[i]:
            tax += (taxBracket[i] - previousBracket) * taxRate[i]
            previousBracket = taxBracket[i]
        else:
            tax += (income - previousBracket) * taxRate[i]
            return tax

    tax += (income - previousBracket) * taxRate[-1]
    return tax
