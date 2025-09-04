import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sharedFunctions import frames, backButton


def taxCalculator(root, mainScreen):
    calculatorFrame = frames(root)

    provinces = StringVar(calculatorFrame)
    provinces.set("Pick a Province or Territory")
    provinceMenu = OptionMenu(calculatorFrame, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories",
                              "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
    provinceMenu.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=5, sticky="nsew")
    provinceMenu.config(font=("Times New Roman", 16))
    provinceMenu["menu"].config(font=("Times New Roman", 16))

    paymentFrequency = StringVar(calculatorFrame)
    paymentFrequency.set("Payment Frequency")
    paymentFrequencyMenu = OptionMenu(calculatorFrame, paymentFrequency, "Daily" ,"Weekly", "Bi-Weekly", "Bi-Monthly", "Monthly", "Annually")
    paymentFrequencyMenu.grid(row=0, column=2, rowspan=2, columnspan=2, padx=10, pady=5, sticky="nsew")
    paymentFrequencyMenu.config(font=("Times New Roman", 16))
    paymentFrequencyMenu["menu"].config(font=("Times New Roman", 16))

    inputLabels = [
        "Income",
        "RRSP Contribution",
        "FHSA Income",
        "Capitol Gains"
    ]

    for index, (text) in enumerate(inputLabels):
        rowNumber = 2 + (index * 2)
        label = tk.Label(calculatorFrame, text=text, font=("Times New Roman", 24), bg="white")
        label.grid(row=rowNumber, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")

    for index, text in enumerate(inputLabels):
        rowNumber = 2 + (index * 2)
        entry = tk.Entry(calculatorFrame, font=("Times New Roman", 24), highlightbackground="black", highlightcolor="black", highlightthickness="2")
        entry.grid(row=rowNumber, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    outputLabels = [
        "Take Home Pay",
        "Gross Income",
        "Provincial Taxes",
        "Federal Taxes",
        "CPP Contributions",
        "EI Contributions",
        "FHSA Deductions",
        "RRSP Deductions"
    ]

    for index, (text) in enumerate(outputLabels):
        rowNumber = index + 2
        label = tk.Label(calculatorFrame, text=text, font=("Times New Roman", 16), bg="white")
        label.grid(row=rowNumber, column=2, padx=10, pady=5, sticky="nsew")

    outputValues = []

    #fix the following

    for index, text in enumerate(outputValues):
        rowNumber = index + 2

        valueLabel = tk.Label(calculatorFrame, text="$ 0.00", font=("Times New Roman", 16), bg="White")
        valueLabel.grid(row=rowNumber, column=3, padx=10, pady=5, sticky="nsew")

        outputValues.append(valueLabel)

    calculateButton = tk.Button(calculatorFrame, text="Calculate!", font=('Times New Roman', 20), command=lambda: calculate())
    calculateButton.grid(row=12, column=1, rowspan=2, columnspan=2, sticky="nsew")

    for i in range(16):
        calculatorFrame.rowconfigure(i, weight=1, uniform="row")
    for j in range(4):
        calculatorFrame.columnconfigure(j, weight=1, uniform="col")

    backButton(calculatorFrame, mainScreen)

    def calculate():

        userProvince = provinces.get()
        if userProvince == "Pick a Province or Territory":
            messagebox.showerror("Input Error", "Please select a province.")
            return

        try:
            userMonthlyIncome = float(monthlyIncome.get().replace(",", "").strip() or 0)
            userRRSPcontribution = float(rrspContribution.get().replace(",", "").strip() or 0)
            userFHSAcontribution = float(fhsaContribution.get().replace(",", "").strip() or 0)
            userCapitalGains = float(capitalGains.get().replace(",", "").strip() or 0)
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
        grossIncome = userMonthlyIncome * 12

        grossIncomeLabel.config(text=f"Gross Income : $ {grossIncome:.2f}")
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
